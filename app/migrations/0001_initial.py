# Generated by Django 5.2 on 2025-04-16 12:49

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
                ('fixt_brand', models.CharField(blank=True, null=True)),
                ('markup', models.FloatField(blank=True, null=True)),
                ('base_trap_price', models.IntegerField(blank=True, null=True)),
                ('base_house_color', models.CharField(blank=True, null=True)),
                ('kitchen_faucet', models.CharField(blank=True, null=True)),
                ('garbage_disposal', models.CharField(blank=True, null=True)),
                ('closet', models.CharField(blank=True, null=True)),
                ('closet_seat', models.CharField(blank=True, null=True)),
                ('pedestal_lav', models.CharField(blank=True, null=True)),
                ('base_pri_lav_faucet', models.CharField(blank=True, null=True)),
                ('base_sec_lav_faucet', models.CharField(blank=True, null=True)),
                ('base_shower_trim', models.CharField(blank=True, null=True)),
                ('base_ts_trim', models.CharField(blank=True, null=True)),
                ('water_heater', models.CharField(blank=True, null=True)),
                ('sewer_line', models.IntegerField(blank=True, null=True)),
                ('water_line', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChinaParts',
            fields=[
                ('model_number', models.CharField(primary_key=True, serialize=False)),
                ('material_type', models.CharField()),
                ('brand', models.CharField()),
                ('collection', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('baker_mitchell', models.FloatField(blank=True, null=True)),
                ('cregger', models.FloatField(blank=True, null=True)),
                ('ferguson', models.FloatField(blank=True, null=True)),
                ('gateway', models.FloatField(blank=True, null=True)),
                ('hubbard', models.FloatField(blank=True, null=True)),
                ('hughes', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField()),
                ('description', models.CharField(blank=True, null=True)),
                ('location', models.CharField(blank=True, null=True)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('model_number', models.CharField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, null=True)),
                ('description', models.CharField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
