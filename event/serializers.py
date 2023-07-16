from .models import *
from students.models import Student
from rest_framework import serializers

class GetStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'department']

class RegistrationSerializer(serializers.ModelSerializer):
    student = GetStudentSerializer(read_only=True)
    class Meta:
        model = Registration
        fields = ['id', 'event_detail', 'student']
        
class NewRegistrationSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):   
        event_detail_id = self.context['event_detail_id']
        self.instance = Registration.objects.create(
            event_detail_id=event_detail_id, **self.validated_data)
        return self.instance
    
    class Meta:
        model = Registration
        fields = ['id', 'event_detail', 'student']
        
        
class EventDetailSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True, read_only=True)
    
    class Meta:
        model = EventDetail
        fields = ['id','venue', 'date', 'capacity', 'event_start_date', 'event_end_date', 'registrations']
        
        
class EventSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    details = EventDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'details']
        
        


class EventDetailInEventSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        event_id = self.context['event_id']
        self.instance = EventDetail.objects.create(
            event_id=event_id, **self.validated_data)
        return self.instance

    class Meta:
        model = EventDetail
        fields = ['venue', 'date', 'capacity',
                  'event_start_date', 'event_end_date']
        