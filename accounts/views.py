from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request, username = username, passwird = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')