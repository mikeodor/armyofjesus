# Generated by Django 3.0.5 on 2020-05-13 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0030_auto_20200512_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='time',
            new_name='The_time',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='day',
        ),
    ]
