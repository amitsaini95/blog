# Generated by Django 3.2.15 on 2022-12-16 09:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20221216_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 9, 45, 1, 758486, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 9, 45, 1, 758539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
