from typing import Dict, Any

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from ecommerceApp.models import ShopUser, Product, Order, OrderItem
from ecommerceApp.serializers import (ShopUserSerializer, ProductSerializer,
                                      OrderSerializer, OrderItemSerializer)


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.all()

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH', 'DISPATCH']:
            return [IsAdminUser()]
        return [AllowAny()]


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ['POST', 'GET']:
            return [IsAuthenticated()]
        print(self.request.data)

        return [IsAdminUser()]

    def get_serializer_context(self):
        if self.request.user:
            user = self.request.user
            return {'user': user}

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user != order.user:
            return Response({"error": "You are not permitted"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user != order.user:
            return Response({"error": "You are not permitted"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user != order.user:
            return Response({"error": "You are not permitted"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class OrderItemModelViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def get_queryset(self):
        user_orders = Order.objects.all().filter(user=self.request.user)
        qs = OrderItem.objects.all().filter(lambda order: order in user_orders)
        return qs

    def get_serializer_context(self):
        if self.request.user:
            user = self.request.user
            return {'user': user}

    def get_permissions(self):
        if self.request.method in ['POST', 'GET']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        print(request.data)
        order_pk = request.data['order']
        order = get_object_or_404(Order, pk=order_pk)
        if order_pk and order:
            if order.user == request.user:
                return super().create(request, *args, **kwargs)

            return Response({"error": "You are not permitted"},
                            status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "You are not permitted"},
                        status=status.HTTP_403_FORBIDDEN)


class CustomTokenObtainViewSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['id'] = self.user.id
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainViewSerializer

