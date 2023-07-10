from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.user}'
