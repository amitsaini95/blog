# Generated by Django 3.2.15 on 2022-12-16 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20221216_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 12, 14, 40, 638012, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 12, 14, 40, 638068, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts1', to='blog.Tag'),
        ),
    ]
