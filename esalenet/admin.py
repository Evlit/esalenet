from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from esalenet.models import Contact, Product, Factory, LevelOneProvider, LevelTwoProvider


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house')
    search_fields = ('email',)
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'view_factory_link')
    search_fields = ('name', 'model')

    def view_factory_link(self, obj):
        from django.utils.html import format_html
        count = obj.factory_set.count()
        url = (
                reverse("admin:esalenet_factory_changelist")
                + "?"
                + urlencode({"product__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Список заводов </a>', url, count)

    view_factory_link.short_description = "Производитель"


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'date_create')
    list_filter = ('contact__city',)


@admin.register(LevelOneProvider)
class LevelOneProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'view_provider_link', 'debt')
    list_filter = ('contact__city',)
    actions = ['reset_debt']

    def reset_debt(self, request, queryset):
        queryset.update(debt=0)
    reset_debt.short_description = "Обнуление задолженности"

    def view_provider_link(self, obj):
        url = (
            reverse("admin:esalenet_factory_changelist") + f"{obj.provider.id}/"
         )
        return format_html('<a href="{}">{}' + f"{obj.provider.name}" + '</a>', url, '')
    view_provider_link.short_description = "Поставщик"


@admin.register(LevelTwoProvider)
class LevelTowProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'view_provider_link', 'debt')
    list_filter = ('contact__city',)
    actions = ['reset_debt']

    def reset_debt(self, request, queryset):
        queryset.update(debt=0)
    reset_debt.short_description = "Обнуление задолженности"

    def view_provider_link(self, obj):
        url = (
            reverse("admin:esalenet_leveloneprovider_changelist") + f"{obj.provider.id}/"
         )
        return format_html('<a href="{}">{}' + f"{obj.provider.name}" + '</a>', url, '')
    view_provider_link.short_description = "Поставщик"
