from django_filters import rest_framework

from esalenet.models import LevelOneProvider, Factory


class LevelOneProviderFilter(rest_framework.FilterSet):
    class Meta:
        model = LevelOneProvider
        fields = {"contact": ("exact", "in")}


class FactoryFilter(rest_framework.FilterSet):
    class Meta:
        model = Factory
        fields = {"contact": ("exact", "in")}
