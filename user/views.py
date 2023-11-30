from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile


def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'profile': profile})

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