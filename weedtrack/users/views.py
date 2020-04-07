from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class TokenValidationView(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        print('token' + token)
        print(request.data)
        try:
            user = Token.objects.get(key=token).user
        except Exception as e:
            return Response({'user': None}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(user)
        return Response({'user': {**serializer.data, 'token': token}})


class TokenValidateView(APIView):
    def get(self, request):
        token = request.data.get('Authorization', '')
        if not token:
            return Response({'user': None}, status=status.HTTP_400_BAD_REQUEST)
        u = User.objects.get(token=token)
        if not u:
            return Response({'user': None}, status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(u)
        return Response({serializer.data})
