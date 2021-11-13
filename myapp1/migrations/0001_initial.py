# Generated by Django 3.2 on 2021-11-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phonenumber', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
            ],
        ),
    ]