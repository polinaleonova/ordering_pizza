from rest_framework import serializers
from .models import Pizza, Order


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('pizza_name', 'description')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pizza_id', 'pizza_size', 'customer_name', 'address')