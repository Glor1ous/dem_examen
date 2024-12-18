# portal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ViolationReportForm
from .models import ViolationReport

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'portal/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reports')
        else:
            return render(request, 'portal/login.html', {'error': 'Invalid credentials'})
    return render(request, 'portal/login.html')

@login_required
def reports(request):
    if request.method == 'POST':
        form = ViolationReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('reports')
    else:
        form = ViolationReportForm()
    reports = ViolationReport.objects.filter(user=request.user)
    return render(request, 'portal/reports.html', {'form': form, 'reports': reports})

@login_required
def admin_panel(request):
    if request.user.username != 'copp':
        return redirect('login')
    reports = ViolationReport.objects.all()
    return render(request, 'portal/admin_panel.html', {'reports': reports})

@login_required
def update_status(request, report_id, status):
    if request.user.username != 'copp':
        return redirect('login')
    report = ViolationReport.objects.get(id=report_id)
    report.status = status
    report.save()
    return redirect('admin_panel')
