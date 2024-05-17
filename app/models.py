from django.db import models

# Create your models here.

# Builder Information
class Builder(models.Model):
    name = models.CharField(max_length=50)
    fixt_brand = models.CharField(null=True, blank=True)
    markup = models.FloatField(null=True, blank=True)
    base_trap_price = models.IntegerField(null=True, blank=True)
    base_house_color = models.CharField(null=True, blank=True)
    kitchen_faucet = models.CharField(null=True, blank=True)
    garbage_disposal = models.CharField(null=True, blank=True)
    closet = models.CharField(null=True, blank=True)
    closet_seat = models.CharField(null=True, blank=True)
    pedestal_lav = models.CharField(null=True, blank=True)
    base_lav_faucet = models.CharField(null=True, blank=True)
    base_shower_trim = models.CharField(null=True, blank=True)
    base_ts_trim = models.CharField(null=True, blank=True)
    water_heater = models.CharField(null=True, blank=True)
    sewer_line = models.IntegerField(null=True, blank=True)
    water_line = models.IntegerField(null=True, blank=True)

# Moen
class Moen(models.Model):
    model_number = models.CharField(primary_key=True)
    material_type = models.CharField()
    collection = models.CharField(null=True, blank=True)
    description = models.CharField()
    finish = models.CharField()
    list_price = models.FloatField()

# Delta
class Delta(models.Model):
    model_number = models.CharField(primary_key=True)
    material_type = models.CharField()
    collection = models.CharField(null=True, blank=True)
    description = models.CharField()
    finish = models.CharField()
    list_price = models.FloatField()

# China Tubs and Showers
class ChinaTubShower(models.Model):
    model_number = models.CharField(primary_key=True)
    material_type = models.CharField()
    brand = models.CharField()
    collection = models.CharField()
    description = models.CharField(null=True, blank=True)
    baker_mitchell = models.FloatField(null=True, blank=True)
    cregger = models.FloatField(null=True, blank=True)
    ferguson = models.FloatField(null=True, blank=True)
    gateway = models.FloatField(null=True, blank=True)
    hubbard = models.FloatField(null=True, blank=True)
    hughes = models.FloatField(null=True, blank=True)

# Misc
class Misc(models.Model):
    model_number = models.CharField(primary_key=True)
    brand = models.CharField(null=True,blank=True)