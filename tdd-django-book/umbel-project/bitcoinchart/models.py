from django.db import models

class Order(models.Model):
    order_type = models.TextField(default='')
    order_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_datetime = models.DateTimeField(auto_now_add=True)