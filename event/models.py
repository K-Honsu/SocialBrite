import uuid
from django.db import models
from students.models import Student

class Event(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class EventDetail(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='details')
    venue = models.CharField(max_length=200)
    date = models.DateField()
    capacity = models.IntegerField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'event -> {self.event.name}'
    
class Registration(models.Model):
    event_detail = models.ForeignKey(EventDetail, on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student} is registered for {self.event_detail.event.name}'