from django.db.models import Count, Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from datetime import datetime
from django.utils.dateparse import parse_date 

from weedtrack.strain_stock.models import StrainStock, StrainOperation
from weedtrack.strain_stock.serializers import StrainOperationSerializer

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

    @action(detail=False, methods=['GET'])
    def consumption(self, request):
        user = request.user
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if not start_date or not end_date:
            return Response({"error": "start_date and end_date query parameters are required and formated "
                             "to YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format"})
        so = StrainOperation.objects.filter(quantity__exact=-0.15, user=user, created_at__lte=end_date, created_at__gte=start_date)
        serializer = StrainOperationSerializer(so, many=True)
        return Response({"operations": len(so), "items": serializer.data}) 

    def _query_by_split(self, query, trunc_function, split):
        return query.annotate(**{split: trunc_function('created_at')})  \
                    .values(split)                                      \
                    .annotate(quantity=Sum('quantity')).values(split, 'quantity')

    @action(detail=False, methods=['GET'])
    def consumption_by_split(self, request):
        user = request.user
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        split = self.request.query_params.get('split', None)

        if not split:
            return Response({"error": "split query parameter is required and must have the value week/day/month"})
        if not start_date or not end_date:
            return Response({"error": "start_date and end_date query parameters are required and formated "
                             "to YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format"})
        
        query = StrainOperation.objects \
            .filter(user=user, quantity__exact=-0.15, created_at__lte=end_date, created_at__gte=start_date)

        if split == 'day':
            so = self._query_by_split(query, TruncDay, split)
        elif split == 'week':
            so = self._query_by_split(query, TruncWeek, split)
        elif split == 'month':
            so = self._query_by_split(query, TruncMonth, split)
        for s in so:
            print(s)
        return Response({"items": so})
