from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StrainStockViewset, StrainOperationViewset 

router = DefaultRouter()
router.register(r'strains', StrainStockViewset, basename='strainstock')
router.register(r'operations', StrainOperationViewset, basename='strainoperation')

urlpatterns = [
        path('', include(router.urls)),
]
