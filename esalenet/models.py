from django.core.validators import MinValueValidator
from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='email address', default='absent@absent.ru')
    country = models.CharField(max_length=50, default='Россия', verbose_name='страна')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица', blank=True, null=True, default=None)
    house = models.SmallIntegerField(verbose_name='номер дома', default=0)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.country}, {self.email}, {self.city}, {self.street}, {self.house}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование товара")
    model = models.CharField(max_length=100, verbose_name='модель товара')
    release_date = models.DateField(blank=True, null=True, default=None, verbose_name='дата выхода')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    contact = models.ForeignKey(Contact, verbose_name="Контакты", on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name="Товары")
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        abstract = True


class Factory(BaseModel):

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.name


class LevelOneProvider(BaseModel):
    provider = models.ForeignKey(Factory, on_delete=models.PROTECT, verbose_name='Поставщик', related_name='factory')
    debt = models.DecimalField(max_digits=9, decimal_places=2, default=0, validators=[MinValueValidator(0)],
                               verbose_name='Задолженность поставщику')

    class Meta:
        verbose_name = "Поставщик первого уровня"
        verbose_name_plural = "Поставщики первого уровня"

    def __str__(self):
        return self.name


class LevelTwoProvider(BaseModel):
    provider = models.ForeignKey(LevelOneProvider, on_delete=models.PROTECT, verbose_name='Поставщик',
                                 related_name='levelone', null=True, blank=True)
    debt = models.DecimalField(max_digits=9, decimal_places=2, default=0, validators=[MinValueValidator(0)],
                               verbose_name='Задолженность поставщику')

    class Meta:
        verbose_name = "Поставщик второго уровня"
        verbose_name_plural = "Поставщики второго уровня"

    def __str__(self):
        return self.name
