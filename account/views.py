from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from account.forms.CustomUserForm import CustomUserForm
from account.forms.CustomUserLoginForm import CustomUserLoginForm
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created!")
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, "account/register.html ", {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in!")
                return redirect('home')
            else: 
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Error username or password")   
    else:
        form = CustomUserLoginForm()
    return render(request, "account/login.html", {"form": form})

def logout_user(request):
    pass