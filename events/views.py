from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventModelSerializer

class EventListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)   
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

class EventRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)      
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
