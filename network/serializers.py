from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from network.models import NetworkElement


class NetworkElementSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        supplier = obj.supplier
        if supplier is None:
            return 0
        if supplier.level == 2:
            raise ValidationError('The object being created is the 4th in the supply chain(max 3). Change the supplier')
        return supplier.level + 1

    class Meta:
        model = NetworkElement
        fields = '__all__'
