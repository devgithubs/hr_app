from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserForm, LoginForm

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:home')
    else:
        form = CustomUserForm()
    
    return render(request, 'register_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('user:register_user')
            else:
                # Authentication failed
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()
        error_message = ''

    return render(request, 'login.html', {'form': form, 'error_message': error_message})