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

    def perform_create(self, serializer):
        strainStock = serializer.save()
        print(serializer.validated_data)
        op = StrainOperation(user=self.request.user, strain=strainStock, quantity=serializer.validated_data['quantity'])
        op.save()
   
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

    def perform_create(self, serializer):
        serializer.save()
        strain = StrainStock.objects.filter(pk=serializer.data['strain'])
        strainobj = strain.first()
        strain.update(quantity=strainobj.quantity + serializer.data['quantity'])
