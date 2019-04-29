# Generated by Django 2.2 on 2019-04-29 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20190429_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(10000)]),
        ),
    ]
