# Generated by Django 3.0.5 on 2020-05-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0006_nextbigevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nextbigevent',
            old_name='NextBigEvent',
            new_name='date',
        ),
        migrations.AddField(
            model_name='nextbigevent',
            name='event',
            field=models.CharField(default='Next Event', max_length=80),
        ),
    ]
