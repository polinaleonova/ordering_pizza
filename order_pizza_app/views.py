from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('customer_name', 'pizza_size')
