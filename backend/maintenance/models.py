from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('bike', 'Bike'),
    ]

    vehicle_no = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    model = models.CharField(max_length=100)
    manufacture_year = models.IntegerField()
    owner = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_no