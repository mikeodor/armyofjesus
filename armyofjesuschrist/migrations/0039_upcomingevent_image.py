# Generated by Django 3.0.5 on 2020-05-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0038_auto_20200514_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevent',
            name='image',
            field=models.ImageField(default='event.jpg', upload_to='eventpic'),
        ),
    ]
