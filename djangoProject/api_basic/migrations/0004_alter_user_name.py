# Generated by Django 3.2 on 2021-04-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
