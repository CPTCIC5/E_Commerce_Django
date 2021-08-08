# Generated by Django 3.2 on 2021-07-23 20:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('pic', models.ImageField(default='default.jpg', upload_to='images')),
                ('desc', models.TextField()),
                ('published_date', models.DateTimeField(default=datetime.datetime(2021, 7, 24, 1, 58, 1, 396793))),
                ('slug', models.SlugField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]