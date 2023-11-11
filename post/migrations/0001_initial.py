# Generated by Django 4.2.7 on 2023-11-11 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('yaratilgan_sana', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]