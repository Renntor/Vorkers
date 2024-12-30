from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views.view_workers import WorkersViewSet, TeamViewSet

app_name = 'api'

router = DefaultRouter()
router.register('worker', WorkersViewSet, basename='worker')
router.register('team', TeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls))
]
