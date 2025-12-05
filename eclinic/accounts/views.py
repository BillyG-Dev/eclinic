from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, LoginForm
from clinicians.forms import ClinicianForm
from patients.forms import PatientForm
from .models import UserProfile

# Choose Role Page
@login_required
def choose_role(request):
    if request.user.userprofile.role == 'clinician':
        return redirect('clinician_dashboard')
    elif request.user.userprofile.role == 'patient':
        return redirect('patient_dashboard')
    return render(request, 'accounts/choose_role.html')

# Patient Signup
def patient_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            user_profile = UserProfile.objects.create(user=user, role='patient')
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        user_form = UserSignupForm()
        patient_form = PatientForm()
    return render(request, 'accounts/patient_signup.html', {'user_form': user_form, 'patient_form': patient_form})

# Clinician Signup
def clinician_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        clinician_form = ClinicianForm(request.POST)
        if user_form.is_valid() and clinician_form.is_valid():
            user = user_form.save()
            user_profile = UserProfile.objects.create(user=user, role='clinician')
            clinician = clinician_form.save(commit=False)
            clinician.user = user
            clinician.save()
            login(request, user)
            return redirect('clinician_dashboard')
    else:
        user_form = UserSignupForm()
        clinician_form = ClinicianForm()
    return render(request, 'accounts/clinician_signup.html', {'user_form': user_form, 'clinician_form': clinician_form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.userprofile.role == 'clinician':
                return redirect('clinician_dashboard')
            elif user.userprofile.role == 'patient':
                return redirect('patient_dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
