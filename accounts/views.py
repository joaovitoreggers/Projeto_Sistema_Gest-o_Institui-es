from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (UserModelSerializer, PasswordResetSerializer, SetNewPasswordSerializer)

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class UserRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_data = {
                'uidb64': uidb64,
                'token': token,
            }
            send_mail(
                'Password Reset Request',
                f'Use este token e User ID para resetar a Senha(enquanto não tem front): {reset_data}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return Response({'message': 'Instruções para a alteração da senha foram enviadas para o seu email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = serializer.validated_data['uidb64']
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']

            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return Response({'error': 'Token, ou ID de usuário inválidos'}, status=status.HTTP_400_BAD_REQUEST)

            if PasswordResetTokenGenerator().check_token(user, token):
                user.set_password(password)
                user.save()
                return Response({'message': 'Senha alterada com sucesso.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Token, ou ID de usuário inválidos'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)