# Generated by Django 5.2 on 2025-04-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=75),
        ),
    ]
