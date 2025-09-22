from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_brand = models.CharField()
    car_model = models.CharField()
    year = models.IntegerField()
    color = models.CharField()
    engine_type = models.CharField()
    fuel_type = models.CharField(
        max_length=20,
        choices=[("Petrol", "Petrol"), ("Diesel", "Diesel"), ("Electric", "Electric"), ("Hybrid", "Hybrid")],
        help_text="Fuel Type"
    )
    transmission = models.CharField(
        max_length=20,
        choices=[("Manual", "Manual"), ("Automatic", "Automatic")],
        help_text="Transmission Type"
    )
    seating_capacity = models.IntegerField(help_text="Number of Seats")
    price = models.CharField()
    mileage = models.CharField()
    description = models.TextField()

    def str(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'year', 'color', 'fuel_type', 'transmission','price','mileage','description')