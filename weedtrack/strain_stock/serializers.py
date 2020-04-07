from rest_framework import serializers
from .models import StrainOperation, StrainStock

class StrainStockSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StrainStock
        fields = ["id", "strainName", "quantity", "user"]

class StrainStockIncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrainStock
        fields = ["id", "strainName"]


class StrainOperationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StrainOperation
        fields = ["id", "strain", "user", "quantity"]

