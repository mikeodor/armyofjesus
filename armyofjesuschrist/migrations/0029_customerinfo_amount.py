# Generated by Django 3.0.5 on 2020-05-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0028_auto_20200512_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='amount',
            field=models.IntegerField(default='1000'),
        ),
    ]
