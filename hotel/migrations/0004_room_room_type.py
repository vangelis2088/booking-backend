# Generated by Django 3.2.17 on 2023-02-11 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='hotel.room_type'),
        ),
    ]
