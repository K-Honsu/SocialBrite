from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('event', views.EventViewSet, basename='event')

event_detail = routers.NestedDefaultRouter(router, 'event', lookup='event')
event_detail.register('details', views.EventDetailViewSet, basename='event-detail')


urlpatterns = router.urls + event_detail.urls
