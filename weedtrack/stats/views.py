from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets 
from weedtrack.strain_stock.serializers import StrainStockSerializer, StrainOperationSerializer

from weedtrack.strain_stock.models import StrainStock, StrainOperation

class StatisticsAPIView(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def test(self, request):
        so = StrainOperation.objects.filter(user=request.user)
        print(so)
        serializer = StrainOperationSerializer(so, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def total(self, request):
        user = request.user
        so = StrainOperation.objects.filter(user=user)
        return Response({"total": len(so)})

    # decorate to get user ?
    @action(detail=False, methods=['GET'])
    def total_by_strain(self, request):
        user = request.user
        output = StrainOperation.objects.filter(user=user).values('strain__strain_name').annotate(Count('id'))
        output = [{'strain_name': strain['strain__strain_name'], 'total': strain['id__count']} for strain in output]
        return Response(output)
