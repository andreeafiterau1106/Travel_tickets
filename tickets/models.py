from django.db import models

class Ticket(models.Model):
    TRANSPORT_CHOICES = [
        ('airplane', 'Airplane')
    ]
    
    airline = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateField()
    duration = models.CharField(max_length=50)
    stopovers = models.BooleanField(default=False)
    special_offer = models.BooleanField(default=False)
    additional_details = models.TextField()
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)

    def __str__(self):
        return f"{self.airline} to {self.destination}"

