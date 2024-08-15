from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostModelSerializer


class PostListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)       
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class PostRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer