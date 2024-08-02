from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event
from .serializers import EventModelSerializer

class EventListCreateView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

class EventRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
