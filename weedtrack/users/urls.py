from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet, UserCreateViewSet, GetCurrentUserView 

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('users', UserCreateViewSet, basename='users')

urlpatterns = [ 
    
    path('users/profile/', GetCurrentUserView.as_view())
]
urlpatterns += router.urls
