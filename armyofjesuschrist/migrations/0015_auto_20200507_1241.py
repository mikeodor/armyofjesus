# Generated by Django 3.0.5 on 2020-05-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0014_auto_20200507_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone_number',
            options={},
        ),
        migrations.AddField(
            model_name='latestsermon',
            name='word',
            field=models.TextField(default='Enter text here', max_length=200),
        ),
    ]
