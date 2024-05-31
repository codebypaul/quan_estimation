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
class ChinaParts(models.Model):
    model_number = models.CharField(primary_key=True)
    material_type = models.CharField()
    brand = models.CharField()
    collection = models.CharField(null=True,blank=True)
    description = models.CharField(null=True, blank=True)
    baker_mitchell = models.FloatField(null=True, blank=True)
    cregger = models.FloatField(null=True, blank=True)
    ferguson = models.FloatField(null=True, blank=True)
    gateway = models.FloatField(null=True, blank=True)
    hubbard = models.FloatField(null=True, blank=True)
    hughes = models.FloatField(null=True, blank=True)

# Combination Pricing
# class TubsShower(models.Model):
#     model_number = models.CharField(primary_key=True)
#     brand = models.CharField()
#     description = models.CharField()
#     base = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)
#     back_wall = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)
#     end_walls = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)
#     wall_set = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)

# class Toilet(models.Model):
#     model_number = models.CharField(primary_key=True)
#     brand = models.CharField()
#     description = models.CharField()
#     bowl = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)
#     tank = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)

# class Lavatory(models.Model):
#     model_number = models.CharField(primary_key=True)
#     brand = models.CharField()
#     description = models.CharField()
#     bowl = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)
#     leg = models.ForeignKey(ChinaParts,on_delete=models.DO_NOTHING)

# Misc
class Misc(models.Model):
    model_number = models.CharField(primary_key=True)
    category = models.CharField(null=True,blank=True)
    brand = models.CharField(null=True,blank=True)
    description = models.CharField(null=True,blank=True)
    price = models.FloatField(null=True,blank=True)

# Labor
class Labor(models.Model):
    category = models.CharField()
    description = models.CharField(null=True, blank=True)
    location = models.CharField(null=True, blank=True)
    price = models.IntegerField()