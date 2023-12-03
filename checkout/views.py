import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Checkout, OrderItem
from basket.models import BasketItem
from django.contrib.auth.decorators import login_required

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
        
        try:
            charge = stripe.Charge.create(
                amount=int(total_price * 100),
                currency='usd',
                description='Dinosaur Purchase',
                source=token,
            )

            checkout = Checkout.objects.create(
                user=request.user,
                email=email,
                username_in_game=username_in_game,
                server=server,                
                total_price=total_price,
                payment_method='Stripe',
                transaction_id=charge.id,
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