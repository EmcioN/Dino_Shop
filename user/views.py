from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Checkout
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def view_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'view_profile.html', {'profile': profile})


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.update_or_create(user=instance)


def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def user_profile(request):
    transactions = Checkout.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'view_profile.html', {'transactions': transactions})
