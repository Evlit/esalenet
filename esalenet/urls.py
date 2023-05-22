from django.urls import path
from esalenet import views

urlpatterns = [
    path("provider1/list", views.LevelOneProviderListView.as_view(), name='provider1-list'),
    path("provider1/<int:pk>", views.LevelOneProviderView.as_view(), name='provider1'),
    path("provider1/create", views.LevelOneProviderCreateView.as_view(), name='provider1-create'),
    path("factory/list", views.FactoryListView.as_view(), name='factory-list'),
    path("factory/<int:pk>", views.FactoryView.as_view(), name='factory'),
    path("factory/create", views.FactoryCreateView.as_view(), name='factory-create'),
]
