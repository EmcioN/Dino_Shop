from .models import BasketItem

def basket_count(request):
    if request.user.is_authenticated:
        count = BasketItem.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'basket_count': count}