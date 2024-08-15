from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import PrjectModelSerializer

class ProjectListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)   
    queryset = Project.objects.all()
    serializer_class = PrjectModelSerializer

class ProjectRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = PrjectModelSerializer