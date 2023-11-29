from django.shortcuts import render
from products.models import Dinosaur

def index(request):    
    most_selling_dinosaur = Dinosaur.objects.order_by('-attack_power').first()
    if not most_selling_dinosaur:
        most_selling_dinosaur = Dinosaur.objects.get(name='T-rex')

    context = {
        'most_selling_dinosaur': most_selling_dinosaur
    }
    return render(request, 'home/index.html', context)    