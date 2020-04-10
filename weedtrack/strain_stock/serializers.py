from rest_framework import serializers
from .models import StrainOperation, StrainStock

class StrainStockSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_strain_name(self, value):
        if StrainStock.objects.filter(strain_name=value).exists():
            raise serializers.ValidationError("Can't have two strains of the same name")
        return value

    class Meta:
        model = StrainStock
        fields = ["id", "strain_name", "quantity", "user"]

class StrainOperationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StrainOperation
        fields = ["id", "strain", "user", "quantity"]

