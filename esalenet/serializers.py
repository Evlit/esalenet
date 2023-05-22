from rest_framework import serializers

from esalenet.models import LevelOneProvider, Factory


class LevelOneProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = LevelOneProvider
        read_only_fields = ("id", "date_create", "debt")
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        read_only_fields = ("id", "date_create")
        fields = "__all__"
