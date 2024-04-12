from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from ecommerceApp.models import ShopUser, Product, Order, OrderItem


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'username', 'email', 'admin']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'