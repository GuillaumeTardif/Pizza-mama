# Generated by Django 4.2.1 on 2023-05-29 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_name_pizza_nnom_rename_price_pizza_prix_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='nnom',
            new_name='nom',
        ),
    ]
