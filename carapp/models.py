from django.db import models

from django.db import models
from django.contrib import admin
class car_inventory(models.Model):
    car_name=models.CharField(max_length=100)
    car_colour=models.CharField(max_length=100)
    car_model=models.CharField(max_length=100)
    car_price=models.IntegerField()
    
    
    def _str_(self):
        return self.car_name
class carAdmin(admin.ModelAdmin):
    list_display=['car_name','car_colour','car_model','car_price']
    search_fields=['car_name','car_colour']
