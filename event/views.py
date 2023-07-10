from .serializers import *
from .models import *
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailViewSet(ModelViewSet):
    def get_queryset(self):
        return EventDetail.objects.filter(event_id=self.kwargs['event_pk'])
    
    def get_serializer_context(self):
        return {'event_id': self.kwargs['event_pk']}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EventDetailInEventSerializer
        return EventDetailSerializer
    
    