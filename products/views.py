from django.shortcuts import render, redirect, get_object_or_404
from .models import Dinosaur, Sale
from .forms import DinosaurForm
from urllib.parse import urlparse, parse_qs
from django.contrib.auth.decorators import login_required, user_passes_test


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
    dinosaur.video_url = convert_youtube_url_to_embed(dinosaur.video_url)
    return render(request, 'item_page.html', {'dinosaur': dinosaur})

def convert_youtube_url_to_embed(url):   
    parsed_url = urlparse(url)    
    query_params = parse_qs(parsed_url.query)    
    video_id = query_params.get('v', [None])[0]    
    if video_id:
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        return embed_url
    else:
        return None

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def delete_dinosaur(request, dinosaur_id):
    dinosaur = get_object_or_404(Dinosaur, id=dinosaur_id)
    if request.method == 'POST':
        dinosaur.delete()
        return redirect('all_dinosaurs')  
    return render(request, 'products/confirm_delete.html', {'dinosaur': dinosaur})

@login_required
@user_passes_test(is_superuser)
def edit_dinosaur(request, dinosaur_id):
    dinosaur = get_object_or_404(Dinosaur, id=dinosaur_id)

    if request.method == 'POST':
        form = DinosaurForm(request.POST, request.FILES, instance=dinosaur)
        if form.is_valid():
            form.save()
            return redirect('all_dinosaurs')  
    else:
        form = DinosaurForm(instance=dinosaur)

    return render(request, 'edit_dinosaur.html', {'form': form})