from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=100,default='Banglore')
    is_reserved = models.BooleanField(default=False)
    reserved_start_time = models.DateTimeField(null=True, blank=True)
    reserved_end_time = models.DateTimeField(null=True, blank=True)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(default=now)

    def duration_in_hours(self):
        return (self.end_time - self.start_time).total_seconds() // 3600

    def calculate_price(self):
        hours = self.duration_in_hours()
        if hours <= 2:
            return 0
        elif hours <= 10:
            return 150 + ((hours - 2) // 2) * 100
        else:
            days = (hours // 24) + (1 if hours % 24 > 0 else 0)
            return days * 500
    feedback = models.TextField(blank=True, null=True)

class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount_paid = models.FloatField(default=0)
    timestamp = models.DateTimeField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)