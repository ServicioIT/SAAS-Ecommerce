# Generated by Django 4.1.7 on 2023-02-14 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)], verbose_name='Price'),
        ),
    ]
