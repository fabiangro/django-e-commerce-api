from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from ecommerceApp.models import ShopUser, Product, Order, OrderItem


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'admin']


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'username', 'email', 'is_staff']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = MainUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['user']
        order = Order.objects.create(user=user, **validated_data)
        return order


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
