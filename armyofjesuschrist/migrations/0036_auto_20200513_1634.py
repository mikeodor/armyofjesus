# Generated by Django 3.0.5 on 2020-05-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0035_auto_20200513_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestsermon',
            name='word',
            field=models.TextField(default='Enter text here'),
        ),
    ]
