from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Project
from .serializers import PrjectModelSerializer

class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = PrjectModelSerializer

class ProjectRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = PrjectModelSerializer