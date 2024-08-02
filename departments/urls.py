from django.urls import path
from .views import DepartmentListCreateView, DepartmentRetriveUpdateDestroyView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='list_create'),
    path('departments/<int:pk>/', DepartmentRetriveUpdateDestroyView.as_view(), name='update'),
]