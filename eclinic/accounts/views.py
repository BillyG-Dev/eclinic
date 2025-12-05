from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import SignupForm, LoginForm

# -------------------------
# SIGN UP VIEW
# -------------------------
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user._role = form.cleaned_data['role']  # BEFORE save!
            user.save()  # Now signal can access _role
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# -------------------------
# LOGIN VIEW
# -------------------------
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('dashboard_redirect')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# -------------------------
# LOGOUT
# -------------------------
def logout_view(request):
    logout(request)
    return redirect('login')
