# Generated by Django 3.2.17 on 2023-02-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('room_description', models.CharField(max_length=200)),
                ('room_price', models.FloatField()),
            ],
        ),
    ]
