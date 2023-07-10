from .serializers import *
from .models import *
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

class StudentViewSet(ListModelMixin,CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateNewStudentSerializer
        return StudentSerializer
    
# class DepartmentViewSet()
