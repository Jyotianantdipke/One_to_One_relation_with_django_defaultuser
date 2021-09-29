from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'Createprofile/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def login_view(request):
    if request.method == 'POST':
        unm = request.POST.get('un')
        pswd = request.POST.get('pw')
        user = authenticate(username=unm, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')

    template_name = 'Createprofile/login.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    template_name = 'Createprofile/home.html'
    context = {}
    return render(request, template_name, context)


@login_required(login_url='login')
def extend_profile_view(request):
    form = UserProfileForm(initial={'user':request.user})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'Createprofile/extendprofile.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login')
def show_profile(request):
    user = request.user
    record = UserProfile.objects.get(user=user)
    print(record)
    context = {'record': record}
    template_name = 'Createprofile/showprofile.html'
    return render(request, template_name, context)


def update_profile(request):
    user = request.user
    record = UserProfile.objects.get(user=user)
    form = UserProfileForm(instance=record)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'Createprofile/extendprofile.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_profile(request):
    user = request.user
    record = UserProfile.objects.get(user=user)
    record.delete()
    logout(request)
    return redirect('register')
