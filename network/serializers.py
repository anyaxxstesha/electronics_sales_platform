from rest_framework import serializers

from network.models import NetworkElement


class NetworkElementSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(read_only=True)
    debt = serializers.DecimalField(decimal_places=2, max_digits=20, read_only=True)

    class Meta:
        model = NetworkElement
        fields = '__all__'
