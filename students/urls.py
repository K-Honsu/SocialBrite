from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')

urlpatterns = router.urls