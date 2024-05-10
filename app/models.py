from django.db import models

# Create your models here.

# Builder Information
class Builder(models.Model):
    name = models.CharField(max_length=50)
    fixt_brand = models.CharField()
    markup = models.FloatField()
    base_trap_price = models.IntegerField()
    base_house_color = models.CharField()
    kitchen_faucet = models.CharField()
    garbage_disposal = models.CharField()
    closet = models.CharField()
    closet_seat = models.CharField()
    pedestal_lav = models.CharField()
    base_lav_faucet = models.CharField()
    base_shower_trim = models.CharField()
    base_ts_trim = models.CharField()
    water_heater = models.CharField()
    sewer_line = models.IntegerField()
    water_line = models.IntegerField()

# Moen
# class Moen(models.Model):
#     model_number = models.CharField()
#     collection = models.CharField()

# Delta
# class Delta(models.Model):
#     model_number = models.CharField()
#     collection = models.CharField()

# China

# Tubs and Showers

# Garbage Disposals
