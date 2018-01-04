from django.db import models

class Order(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)