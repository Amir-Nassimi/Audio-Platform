from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OfflineVoiceDetectionViewSet

router = DefaultRouter()

router.register(r'voice-detection/(?P<voice_id>\d+)', OfflineVoiceDetectionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
