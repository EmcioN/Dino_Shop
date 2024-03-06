import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Checkout, OrderItem
from basket.models import BasketItem
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    total_price = sum(item.dinosaur.price * item.quantity for item in basket_items)

    if request.method == 'POST':
        username_in_game = request.POST.get('username_in_game')
        server = request.POST.get('server')
        email = request.POST.get('email')
        token = request.POST.get('stripeToken')
        transaction_id = get_random_string(32)

        try:
            payment_intent = create_payment_intent_with_metadata(
                transaction_id,
                int(total_price * 100),
                'usd'
            )

            checkout = Checkout.objects.create(
                user=request.user,
                email=email,
                username_in_game=username_in_game,
                server=server,
                total_price=total_price,
                payment_method='Stripe',
                transaction_id=transaction_id,
            )

            for item in basket_items:
                OrderItem.objects.create(
                    checkout=checkout,
                    dinosaur=item.dinosaur,
                    quantity=item.quantity,
                )

            basket_items.delete()

            return redirect('checkout_success')

        except stripe.error.StripeError as e:
            return render(request, 'checkout/error.html', {'message': str(e)})

    context = {
        'basket_items': basket_items,
        'total_price': total_price,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request):
    return render(request, 'checkout/success.html')


def create_payment_intent_with_metadata(transaction_id, amount, currency="usd"):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        metadata={"transaction_id": transaction_id}
    )