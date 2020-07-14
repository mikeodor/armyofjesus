# Generated by Django 3.0.5 on 2020-05-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyofjesuschrist', '0017_auto_20200507_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='pastors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=20)),
                ('image', models.ImageField(default='pastor.jpg', upload_to='pastors_pic')),
            ],
            options={
                'verbose_name_plural': 'Pastors',
            },
        ),
    ]
