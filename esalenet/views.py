from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from esalenet.filters import LevelOneProviderFilter, FactoryFilter
from esalenet.models import LevelOneProvider, LevelTwoProvider, Factory
from esalenet.serializers import LevelOneProviderSerializer, FactorySerializer


class LevelOneProviderListView(ListAPIView):
    model = LevelOneProvider
    queryset = LevelOneProvider.objects.exclude(name='Нет поставщика')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LevelOneProviderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LevelOneProviderFilter


class LevelOneProviderView(RetrieveUpdateDestroyAPIView):
    model = LevelOneProvider
    queryset = LevelOneProvider.objects.all()
    serializer_class = LevelOneProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        not_exist = LevelOneProvider.objects.get(name='Нет поставщика')
        with transaction.atomic():
            LevelTwoProvider.objects.filter(provider=instance.id).update(provider_id=not_exist.id)
        instance.delete()


class LevelOneProviderCreateView(CreateAPIView):
    model = LevelOneProvider
    serializer_class = LevelOneProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


class FactoryListView(ListAPIView):
    model = Factory
    queryset = Factory.objects.exclude(name='Нет завода')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactoryFilter


class FactoryView(RetrieveUpdateDestroyAPIView):
    model = Factory
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        not_exist = Factory.objects.get(name='Нет завода')
        with transaction.atomic():
            LevelOneProvider.objects.filter(provider=instance.id).update(provider_id=not_exist.id)
        instance.delete()


class FactoryCreateView(CreateAPIView):
    model = Factory
    serializer_class = FactorySerializer
    permission_classes = [permissions.IsAuthenticated]
