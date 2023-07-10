from .models import *
from rest_framework import serializers

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetail
        fields = ['id','venue', 'date', 'capacity', 'event_start_date', 'event_end_date']
        
        
class EventSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    details = EventDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'details']
        
        

class EventDetailInEventSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        event_id = self.context['event_id']
        # venue = self.validated_data['venue']
        # date = self.validated_data['date']
        self.instance = EventDetail.objects.create(
            event_id=event_id, **self.validated_data)
        return self.instance

    class Meta:
        model = EventDetail
        fields = ['venue', 'date', 'capacity',
                  'event_start_date', 'event_end_date']