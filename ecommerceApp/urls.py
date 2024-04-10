from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('products', views.ProductModelViewSet)

urlpatterns = [
    # path('user', views.user_api),
    # path('user/<int:pk>', views.user_api),
    # path('products', views.ProductList.as_view()),
    # path('product/<int:pk>', views.ProductDetail.as_view())
    path('', include(router.urls))
]
