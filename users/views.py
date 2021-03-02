from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls.base import reverse
from .forms import CustomUserCreationForm

def dashboard(request):
    context = {}
    return render(request, 'users/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('users:dashboard'))
        return render(request, 'users/register.html', context={'form': form})
    form = CustomUserCreationForm()
    return render(request, 'users/register.html', context={'form': form})
    
