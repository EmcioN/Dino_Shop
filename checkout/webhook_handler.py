from django.http import JsonResponse
from .models import Checkout
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

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
        transaction_id = metadata.get('transaction_id')

        try:
            checkout = Checkout.objects.get(transaction_id=transaction_id)
            checkout.status = 'Completed'
            checkout.save()
        except Checkout.DoesNotExist:
            logger.error('Checkout instance not found for transaction_id: %s', transaction_id)


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
        transaction_id = metadata.get('transaction_id')

        try:
            checkout = Checkout.objects.get(transaction_id=transaction_id)
            checkout.status = 'Failed'
            checkout.save()
        except Checkout.DoesNotExist:
            logger.error('Checkout instance not found for transaction_id: %s', transaction_id)


        subject = "Payment failed"
        message = f"Dear {username_in_game},\n\nUnfortunately, your payment for the server {server} has failed. Please try again or contact support for assistance."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

        return JsonResponse({'status': 'success', 'message': 'PaymentIntent failed received'}, status=200)

    def handle_charge_succeeded(self, event):
        charge = event['data']['object']
        transaction_id = charge['id']

        try:
            checkout = Checkout.objects.get(transaction_id=transaction_id)
            checkout.status = 'Completed'
            checkout.save()

            email = checkout.email
            subject = "Your payment was successful!"
            message = f"Dear {checkout.username_in_game},\n\nYour payment for the server {checkout.server} was successful. Thank you for your purchase."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            return JsonResponse({'status': 'success', 'message': 'Charge succeeded received and handled'}, status=200)
        except Checkout.DoesNotExist:
            logger.error('Checkout instance not found for transaction_id: %s', transaction_id)
            return JsonResponse({'status': 'error', 'message': 'Checkout not found'}, status=400)