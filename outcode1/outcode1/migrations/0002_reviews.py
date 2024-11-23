# Generated by Django 5.1.3 on 2024-11-23 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outcode1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outcode1.hotel')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outcode1.room')),
            ],
        ),
    ]
