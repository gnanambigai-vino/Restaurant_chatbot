# chatbotapp/models.py
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('packing', 'Packing'),
        ('waiting_for_service', 'Waiting for Service'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    
    user_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='preparing')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name} - {self.item} - {self.status}"
