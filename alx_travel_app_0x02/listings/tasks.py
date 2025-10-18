from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_payment_confirmation_email(user_email):
    send_mail(
        'Payment Confirmation',
        'Your payment has been successfully completed.',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )
