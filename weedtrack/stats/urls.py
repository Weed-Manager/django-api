from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatisticsAPIView

router = DefaultRouter()
router.register(r'stats', StatisticsAPIView, basename='statistics')
urlpatterns = [
    path('', include(router.urls)),
]
