from django.db.models import Count, Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets 
from weedtrack.strain_stock.serializers import StrainStockSerializer, StrainOperationSerializer

from weedtrack.strain_stock.models import StrainStock, StrainOperation

class StatisticsAPIView(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def total(self, request):
        user = request.user
        so = StrainOperation.objects.filter(user=user, quantity__lt=0).aggregate(Sum('quantity'))
        return Response({"total": abs(so['quantity__sum'])})

    @action(detail=False, methods=['GET'])
    def total_by_strain(self, request):
        user = request.user
        output = StrainOperation.objects.filter(user=user, quantity__lt=0).values('strain__strain_name').annotate(quantity=Sum('quantity'))
        output_list = []
        for strain in output:
            output_list.append({'strain_name': strain['strain__strain_name'], 'total': abs(strain['quantity'])})
        strain_list = StrainStock.objects.filter(user=user)
        self.add_empty_strains(output_list, strain_list)
        return Response(output_list)
 
    @action(detail=False, methods=['GET'])
    def total_caps_by_strain(self, request):
        user = request.user
        output = StrainOperation.objects.filter(user=user, quantity=-0.15).values('strain__strain_name').annotate(Count('id'))
        output = [{'strain_name': strain['strain__strain_name'], 'total_caps': strain['id__count']} for strain in output]
        strain_list = StrainStock.objects.filter(user=user)
        self.add_empty_strains(output, strain_list, 'total_caps')
        return Response(output)

    def add_empty_strains(self, querry_list, strain_list, total_field_name='total'):
        strain_list = (list(strain_list))
        consumed_strains = [s['strain_name'] for s in querry_list]
        for s in strain_list:
            if s.strain_name not in consumed_strains:
                querry_list.append({'strain_name': s.strain_name, total_field_name: 0})

    @action(detail=False, methods=['GET'])
    def total_caps(self, request):
        user = request.user
        so = StrainOperation.objects.filter(user=user, quantity__lt=-0.14, quantity__gt=-0.16).aggregate(Count('quantity'))
        return Response({"total_caps": abs(so['quantity__count'])})
