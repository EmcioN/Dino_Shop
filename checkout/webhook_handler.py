from django.http import JsonResponse
from .models import Checkout
from django.core.mail import send_mail
from django.conf import settings


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return JsonResponse({'status': 'success', 'message': 'Unhandled event received'}, status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        metadata = intent.get('metadata', {})
        email = metadata.get('email', 'No email provided')
        username_in_game = metadata.get('username_in_game', 'No username provided')
        server = metadata.get('server', 'No server provided')
        subject = "Your payment was successful!"
        message = f"Dear {username_in_game},\n\nYour payment for the server {server} was successful. Thank you for your purchase."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

        return JsonResponse({'status': 'success', 'message': 'PaymentIntent succeeded received'}, status=200)

    def handle_payment_intent_payment_failed(self, event):
        intent = event.data.object
        metadata = intent.get('metadata', {})
        email = metadata.get('email', 'No email provided')
        username_in_game = metadata.get('username_in_game', 'No username provided')
        server = metadata.get('server', 'No server provided')
        subject = "Payment failed"
        message = f"Dear {username_in_game},\n\nUnfortunately, your payment for the server {server} has failed. Please try again or contact support for assistance."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

        return JsonResponse({'status': 'success', 'message': 'PaymentIntent failed received'}, status=200)
