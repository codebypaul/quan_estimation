# Generated by Django 5.0.3 on 2024-05-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fixt_brand', models.CharField()),
                ('markup', models.FloatField()),
                ('base_trap_price', models.IntegerField()),
                ('base_house_color', models.CharField()),
                ('kitchen_faucet', models.CharField()),
                ('garbage_disposal', models.CharField()),
                ('closet', models.CharField()),
                ('closet_seat', models.CharField()),
                ('pedestal_lav', models.CharField()),
                ('base_lav_faucet', models.CharField()),
                ('base_shower_trim', models.CharField()),
                ('base_ts_trim', models.CharField()),
                ('water_heater', models.CharField()),
                ('sewer_line', models.IntegerField()),
                ('water_line', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChinaTubShower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField()),
                ('material_type', models.CharField()),
                ('brand', models.CharField()),
                ('collection', models.CharField()),
                ('baker_mitchell', models.FloatField()),
                ('cregger', models.FloatField()),
                ('ferguson', models.FloatField()),
                ('gateway', models.FloatField()),
                ('hubbard', models.FloatField()),
                ('hughes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Delta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField()),
                ('material_type', models.CharField()),
                ('collection', models.CharField()),
                ('description', models.CharField()),
                ('finish', models.CharField()),
                ('list_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Moen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField()),
                ('material_type', models.CharField()),
                ('collection', models.CharField()),
                ('description', models.CharField()),
                ('finish', models.CharField()),
                ('list_price', models.FloatField()),
            ],
        ),
    ]
