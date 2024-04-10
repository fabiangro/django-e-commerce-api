from rest_framework import serializers
from ecommerceApp.models import User, Product, Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'