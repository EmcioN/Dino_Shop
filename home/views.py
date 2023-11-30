from django.shortcuts import render, redirect
from products.models import Dinosaur
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import ContactMessage, PatchNote

def index(request):    
    most_selling_dinosaur = Dinosaur.objects.order_by('-attack_power').first()
    if not most_selling_dinosaur:
        most_selling_dinosaur = Dinosaur.objects.get(name='T-rex')

    context = {
        'most_selling_dinosaur': most_selling_dinosaur
    }
    return render(request, 'home/index.html', context)    

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            ContactMessage.objects.create(
                user=request.user,
                subject=subject,
                message=message
            )

            send_mail(subject, message, request.user.email, ['your_email@example.com'])
            
            return redirect('success_url')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def success(request):
    return render(request, 'home/success.html')

def patch_notes(request):
    notes = PatchNote.objects.all().order_by('-created_at')
    return render(request, 'news/patch_notes.html', {'notes': notes})    