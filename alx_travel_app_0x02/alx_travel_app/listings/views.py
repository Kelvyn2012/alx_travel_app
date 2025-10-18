from rest_framework import viewsets
from django.http import HttpResponse
from .models import Listing, Booking,Payment
from .serializers import ListingSerializer, BookingSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import send_payment_confirmation_email
import requests

CHAPA_URL = "https://api.chapa.co/"

CHAPA_URL = "https://api.chapa.co/"

@api_view(['POST'])
def initiate_payment(request):
    booking_reference = request.data.get("booking_reference")
    amount = request.data.get("amount")
    user_email = request.data.get("email")  # Retrieve the email from the request data
    
    # Data to send to Chapa API
    payment_data = {
        "amount": amount,
        "email": user_email,
        "phone": request.data.get("phone"),
        "redirect_url": "http://your_redirect_url.com",
        "order_id": booking_reference,
    }
    
    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }
    
    response = requests.post(f"{CHAPA_URL}/payment/initialize/", json=payment_data, headers=headers)

    if response.status_code == 200:
        data = response.json()
        transaction_id = data['data']['transaction_id']
        
        # Store payment in the database
        payment = Payment.objects.create(
            booking_reference=booking_reference,
            payment_status="Pending",
            amount=amount,
            transaction_id=transaction_id,
            user_email=user_email  # Save the email in the Payment model (if you have this field)
        )
        
        return Response({"payment_url": data['data']['payment_url'], "transaction_id": transaction_id}, status=200)
    
    return Response({"error": "Payment initiation failed"}, status=400)

@api_view(['GET'])
def verify_payment(request, transaction_id):
    # Verify the transaction with Chapa
    headers = {
        "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
    }
    
    response = requests.get(f"{CHAPA_URL}/payment/verify/{transaction_id}/", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        payment = Payment.objects.get(transaction_id=transaction_id)
        
        # Update payment status based on Chapa response
        if data['data']['status'] == 'successful':
            payment.payment_status = "Completed"
        else:
            payment.payment_status = "Failed"
        
        payment.save()
        
        # Send confirmation email if payment is successful
        if payment.payment_status == "Completed":
            send_payment_confirmation_email.delay(payment.user_email)  # Use the saved user email
        
        return Response({"status": payment.payment_status}, status=200)
    
    return Response({"error": "Payment verification failed"}, status=400)

def home(request):
    return HttpResponse("Welcome to ALX Travel App v2!")


class ListingViewSet(viewsets.ModelViewSet):
    """API endpoint for managing Listings"""

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """API endpoint for managing Bookings"""

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




