# Generated by Django 3.2.15 on 2022-12-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_user_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profileimage',
            field=models.ImageField(upload_to='images'),
        ),
    ]
