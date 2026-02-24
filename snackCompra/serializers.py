from rest_framework import serializers
from snackCompra.models import SnackCompra


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackCompra
        fields = '__all__'