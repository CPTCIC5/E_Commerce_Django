# Generated by Django 3.2 on 2021-07-29 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210729_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name_plural': 'Seller'},
        ),
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 23, 42, 34, 481476)),
        ),
    ]
