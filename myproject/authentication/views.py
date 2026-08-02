from django.shortcuts import redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url or 'book')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


# Logout
def logout_view(request):
    logout(request)
    return redirect('home')  