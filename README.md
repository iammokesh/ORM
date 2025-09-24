# Ex02 Django ORM Web Application
# Date:24.09.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
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
from django.contrib import admin
from django.contrib import admin
from .models import car_inventory,carAdmin    
admin.site.register(car_inventory,carAdmin)
# Register your models here.
```
# OUTPUT
[alt text](<../Screenshot (5).png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
