from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from ecommerceApp.models import ShopUser, Product, Order, OrderItem
from ecommerceApp.serializers import (ShopUserSerializer, ProductSerializer,
                                      OrderSerializer, OrderItemSerializer)


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
#
# class ProductList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#
# class ProductDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def user_api(request, pk=None):
#     if request.method == 'GET':
#         if pk:
#             user = get_object_or_404(User, pk=pk)
#             user_serializer = UserSerializer(user)
#             return JsonResponse(user_serializer.data, safe=False)
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return JsonResponse(users_serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#
#     elif request.method == 'PUT':
#         user_data = JSONParser().parse(request)
#         user = User.objects.get(pk=user_data['id'])
#         user_serializer =  UserSerializer(user, data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("Update Successfully", safe=False)
#         return JsonResponse("Failed to update")
#
#     elif request.method == "DELETE":
#         user = get_object_or_404(User, pk=pk)
#         user.delete()
#         return JsonResponse("Deleted Successfully")
#
#
# @api_view(['GET'])
# def products_api(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         products_serializer = ProductSerializer(products, many=True)
#         return JsonResponse(products_serializer.data, safe=False)
#
#
# @api_view(['GET'])
# def product_api(request, pk):
#     if request.method == 'GET':
#         product = get_object_or_404(Product, pk=pk)
#         product_serializer = ProductSerializer(product)
#         return JsonResponse(product_serializer.data, safe=False)