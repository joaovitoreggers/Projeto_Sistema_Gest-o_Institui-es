from django.urls import path
from .views import EventListCreateView, EventRetriveUpdateDestroyView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event_list_create'),
    path('events/<int:pk>/', EventRetriveUpdateDestroyView.as_view(), name='event_update'),
]
