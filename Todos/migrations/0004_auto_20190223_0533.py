# Generated by Django 2.1.7 on 2019-02-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todos', '0003_auto_20190222_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='Task',
            field=models.TextField(max_length=200),
        ),
    ]
