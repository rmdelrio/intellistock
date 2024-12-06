from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, VendorViewSet, ItemViewSet,
    DailySalesViewSet, MonthlySalesViewSet, OrderViewSet,
    OrderItemViewSet, DeliveryViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'items', ItemViewSet)
router.register(r'daily-sales', DailySalesViewSet)
router.register(r'monthly-sales', MonthlySalesViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet) 
router.register(r'deliveries', DeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
