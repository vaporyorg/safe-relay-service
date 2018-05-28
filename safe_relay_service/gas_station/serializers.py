from rest_framework import serializers


class GasPriceSerializer(serializers.Serializer):
    lowest = serializers.CharField(max_length=20)
    safe_low = serializers.CharField(max_length=20)
    standard = serializers.CharField(max_length=20)
    fast = serializers.CharField(max_length=20)
    fastest = serializers.CharField(max_length=20)
