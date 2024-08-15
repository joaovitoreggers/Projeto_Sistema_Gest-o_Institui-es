from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Department
from.serializers import DepartmentModelSerializer

class DepartmentListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)   
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class DepartmentRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer