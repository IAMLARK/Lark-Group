from django.db import models

class Booking(models.Model):
    device_name = models.CharField(max_length=100)
    repair_status = models.CharField(max_length=100)
    
    class Meta:
        permissions = [
            ('view_dashboard', 'Can View Dashboard'),
            ('book_device', 'Can Book Device'),
            ('update_repair_status', 'Can Update Repair Status'),
            ('see_booking_available', 'Can See Booking Available'),
        ]
