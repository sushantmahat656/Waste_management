from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in!!")
            email_domain = username.split('@')[-1]
            return render(request, 'home.html', {'email_domain': email_domain})
            #return redirect('home')
        else:
            messages.success(request, "Error logging in. Re-try again later...")
            return redirect('home')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out ...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Authentication
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=email, password=password)
                login(request, user)
                messages.success(request, "You have successfully registered.")
                return redirect('login_user')
            except IntegrityError:
                messages.error(request, "This email address is already in use. Please use a different email.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})