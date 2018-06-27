from django.shortcuts import render
from rest_framework import viewsets

from .models import Pizza, Order
from .serializers import PizzaSerializer, OrderSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to add, edit and remove pizza.
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to add, edit and remove order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


