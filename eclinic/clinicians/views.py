from django.shortcuts import render, redirect
from .forms import ClinicianForm
from .models import Clinician
from django.contrib.auth.decorators import login_required
from accounts.decorators import clinician_required

@clinician_required
def clinician_profile(request):
    clinician = Clinician.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClinicianForm(request.POST, instance=clinician)
        if form.is_valid():
            form.save()
            return redirect('clinician_dashboard')
    else:
        form = ClinicianForm(instance=clinician)
    return render(request, 'clinicians/clinician_profile.html', {'form': form})

