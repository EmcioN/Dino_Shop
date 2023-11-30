from django.shortcuts import get_object_or_404, render, redirect
from .models import BasketItem
from products.models import Dinosaur
from django.contrib.auth.decorators import login_required

def view_basket(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.dinosaur.price for item in basket_items)

    context = {
        'basket_items': basket_items,
        'total_price': total_price
    }
    return render(request, 'basket.html', context)

@login_required
def add_to_basket(request, dinosaur_id):
    dinosaur = Dinosaur.objects.get(id=dinosaur_id)
    BasketItem.objects.create(user=request.user, dinosaur=dinosaur, quantity=1)
    return redirect('all_dinosaurs')

def increase_quantity(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_basket')

def decrease_quantity(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id, user=request.user)
    item.quantity -= 1
    if item.quantity <= 0:
        item.delete()
    else:
        item.save()
    return redirect('view_basket')
