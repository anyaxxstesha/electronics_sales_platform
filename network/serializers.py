from rest_framework import serializers

from network.models import NetworkElement


class NetworkElementSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        supplier = obj.supplier
        if supplier is None:
            return 0
        return supplier.level + 1

    class Meta:
        model = NetworkElement
        fields = '__all__'
