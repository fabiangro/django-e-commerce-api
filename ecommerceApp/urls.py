from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CustomTokenObtainPairView

router = DefaultRouter()
router.register('products', views.ProductModelViewSet)
router.register('orders', views.OrderModelViewSet,
                basename='orders')
router.register('orderitems', views.OrderItemModelViewSet,
                basename='order_items')

urlpatterns = [
    # path('user', views.user_api),
    # path('user/<int:pk>', views.user_api),
    # path('products', views.ProductList.as_view()),
    # path('product/<int:pk>', views.ProductDetail.as_view())
    path('', include(router.urls)),
    path('auth/login', CustomTokenObtainPairView.as_view(),
         name='custom_token_obtain_pair')
]
