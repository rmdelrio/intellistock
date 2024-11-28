from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
