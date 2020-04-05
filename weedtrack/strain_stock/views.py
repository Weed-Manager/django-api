from django.shortcuts import render
from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from .models import StrainStock, StrainOperation
from weedtrack.users.models import User
from .serializers import StrainStockSerializer, StrainOperationSerializer

# Create your views here.

class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass

class StrainStockViewset(CreateListRetrieveViewSet):
    serializer_class = StrainStockSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        return Response(serializer.errors)
    
    def get_queryset(self):
        user = self.request.user
        items = StrainStock.objects.filter(user=user)
        print(user)
        return items

class StrainOperationViewset(CreateListRetrieveViewSet):
    serializer_class = StrainOperationSerializer

    def get_queryset(self):
        user = self.request.user
        items = StrainOperation.objects.filter(user=user)
        return items

