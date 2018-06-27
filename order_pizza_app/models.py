from django.db import models

pizza_sizes = (
    ("30cm", "30cm"),
    ("50cm", "50cm")
)


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)


class Order(models.Model):
    pizza_id = models.ForeignKey(Pizza, related_name='ordered', blank=False, null =False, on_delete=models.CASCADE)
    pizza_size = models.CharField(max_length=255, choices=pizza_sizes, default="30cm")
    customer_name = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
