from .models import *
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']
        
        
class StudentSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(read_only=True)
    department = DepartmentSerializer()
    class Meta:
        model = Student
        fields = ['id','user', 'matric_no', 'department']
        
class CreateNewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user', 'matric_no', 'department']
        