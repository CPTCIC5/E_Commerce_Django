# Generated by Django 3.2 on 2021-07-29 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_product_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 0, 11, 37, 172983)),
        ),
    ]