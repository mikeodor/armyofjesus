# Generated by Django 3.0.5 on 2020-05-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0020_latestsermon_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestsermon',
            name='audio',
            field=models.FileField(default='sermondefault', upload_to='sermon_audio'),
        ),
    ]
