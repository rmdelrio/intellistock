from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'daily-sales', DailySalesViewSet)
router.register(r'monthly-sales', MonthlySalesViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'stores', StoreViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
