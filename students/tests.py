# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Student, Department
# from users.models import UserAccount
# from .serializers import StudentSerializer
# from django.contrib.auth import get_user_model
# # user = get_user_model()


# class StudentViewSetTests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.department = Department.objects.create(name='Computer Science')
#         self.user = UserAccount.objects.create(
#             username='test_user', password='test_password', email='testuser@example.com')

#     def test_create_student(self):
#         data = {
#             'user': self.user.id,
#             'matric_no': '123456789',
#             'department': self.department.id,
#         }
#         response = self.client.post('/students/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         student = Student.objects.get(pk=response.data['id'])
#         self.assertEqual(student.matric_no, data['matric_no'])
#         self.assertEqual(student.department, self.department)

#     def test_retrieve_student(self):
#         student = Student.objects.create(
#             user=self.user, matric_no='123456789', department=self.department
#         )
#         response = self.client.get('/students/{}/'.format(student.id))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['matric_no'], student.matric_no)

#     def test_update_student(self):
#         student = Student.objects.create(
#             user=self.user, matric_no='123456789', department=self.department
#         )
#         data = {'matric_no': '987654321'}
#         response = self.client.put(
#             '/students/{}/'.format(student.id), data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         student.refresh_from_db()
#         self.assertEqual(student.matric_no, data['matric_no'])

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student, Department
from users.models import UserAccount


class StudentViewSetTests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Computer Science')
        self.user = UserAccount.objects.create(
            username='test_user', password='test_password', email='testuser@example.com'
        )

    def test_create_student(self):
        url = reverse('student-list')  # Use the viewset name for the URL
        data = {
            'user': self.user.id,
            'matric_no': '123456789',
            'department': self.department.id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        student = Student.objects.get(pk=response.data['id'])
        self.assertEqual(student.matric_no, data['matric_no'])
        self.assertEqual(student.department, self.department)

    def test_retrieve_student(self):
        student = Student.objects.create(
            user=self.user, matric_no='123456789', department=self.department
        )
        # Use the viewset name for the URL
        url = reverse('student-detail', args=[student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['matric_no'], student.matric_no)

    def test_update_student(self):
        student = Student.objects.create(
            user=self.user, matric_no='123456789', department=self.department
        )
        # Use the viewset name for the URL
        url = reverse('student-detail', args=[student.id])
        data = {'matric_no': '987654321'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        student.refresh_from_db()
        self.assertEqual(student.matric_no, data['matric_no'])
        self.assertEqual(student.department, self.department)
