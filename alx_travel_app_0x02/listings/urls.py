from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet,initiate_payment,verify_payment

router = DefaultRouter()
router.register(r"listings", ListingViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.home, name="home"),  # root URL
    path('payment/initiate/', initiate_payment, name='initiate_payment'),
    path('payment/verify/<str:transaction_id>/', verify_payment, name='verify_payment'),
]



