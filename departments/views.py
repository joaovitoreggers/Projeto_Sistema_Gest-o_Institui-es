from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Department
from.serializers import DepartmentModelSerializer

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class DepartmentRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer