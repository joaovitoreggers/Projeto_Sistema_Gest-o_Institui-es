from django.urls import path
from .views import ProjectListCreateView, ProjectRetriveUpdateDestroyView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='projects_list_create'),
    path('orojects/<int:pk>/', ProjectRetriveUpdateDestroyView.as_view(), name='project_update')
]
