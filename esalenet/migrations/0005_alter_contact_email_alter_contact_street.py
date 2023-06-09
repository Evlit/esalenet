# Generated by Django 4.2.1 on 2023-05-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("esalenet", "0004_alter_contact_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(
                default="absent@absent.ru", max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="street",
            field=models.CharField(
                blank=True, default=None, max_length=50, null=True, verbose_name="улица"
            ),
        ),
    ]
