# Generated by Django 3.2 on 2021-11-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='avatar',
            field=models.TextField(default='No Description'),
        ),
    ]