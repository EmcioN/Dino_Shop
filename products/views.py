from django.shortcuts import render, redirect, get_object_or_404
from .models import Dinosaur, Sale
from .forms import DinosaurForm

def all_dinosaurs(request):    
    dinosaurs = Dinosaur.objects.all()
    
    context = {
        'dinosaurs': dinosaurs
    }
    
    return render(request, 'products/products.html', context)

def add_dinosaur(request):
    if request.method == 'POST':
        form = DinosaurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_dinosaurs')
    else:
        form = DinosaurForm()
    
    return render(request, 'products/add_dinosaur.html', {'form': form})

def item_page(request, dinosaur_id):
    dinosaur = get_object_or_404(Dinosaur, id=dinosaur_id)
    return render(request, 'item_page.html', {'dinosaur': dinosaur})    