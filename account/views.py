from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms.CustomUserForm import CustomUserForm
from account.forms.CustomUserLoginForm import CustomUserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            # Vérifiez si le nom d'utilisateur existe déjà
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')
                return redirect('register_user')
            
            # Vérifiez si l'email existe déjà (facultatif)
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà utilisé. Veuillez en choisir un autre.')
                return redirect('register_user')
            
            form.save()
            messages.success(request, "Votre compte a été créé avec succès!")
            return redirect('login_user')
    else:
        form = CustomUserForm()
    return render(request, "account/register.html", {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Vous êtes connecté!")
                return redirect('home')
            else: 
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide")
        else:
            messages.error(request, "Erreur de nom d'utilisateur ou de mot de passe")   
    else:
        form = CustomUserLoginForm()
    return render(request, "account/login.html", {"form": form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Vous êtes déconnecté!")
    return redirect('home')
