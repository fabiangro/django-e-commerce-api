from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from ecommerceApp.models import User, Product, Order, OrderItem
from ecommerceApp.serializers import (UserSerializer, ProductSerializer,
                                      OrderSerializer, OrderItemSerializer)


# @csrf_exempt
@api_view(['GET', 'POST'])
def user_api(request, pk=None):
    if request.method == 'GET':
        if pk:
            user = get_object_or_404(User, pk=pk)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(pk=user_data['id'])
        user_serializer =  UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == "DELETE":
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return JsonResponse("Deleted Successfully")