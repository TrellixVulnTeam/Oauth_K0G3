# Generated by Django 2.1.7 on 2019-02-27 11:34

import datetime
from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]