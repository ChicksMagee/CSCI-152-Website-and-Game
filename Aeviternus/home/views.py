from django.shortcuts import render, redirect
from home.forms import (
    RegistrationForm,
    ContactModelForm,
    EditProfileModelForm)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Post
from django.utils import timezone
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/home.html', {'posts': posts})

def about(request):
    return render(request, 'home/about.html')

def account(request):
    return render(request, 'home/account.html')

def buyNow(request):
    return render(request, 'home/buy-now.html')

def buyForm(request):
    return render(request, 'home/buy-form.html')

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:

            args = {'form': form}
            return render(request, 'home/reg_form.html', args)
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'home/reg_form.html', args)


def contact(request):
    if request.method=='POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:

            args = {'form': form}
            return render(request, 'home/contact.html', args)

    else:
        form = ContactModelForm()

        args = {'form': form}
        return render(request, 'home/contact.html', args)


def edit_profile(request):
    if request.method=='POST':
        form = EditProfileModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/home/account/')
        else:

            args = {'form': form}
            return render(request, 'home/edit_profile.html', args)

    else:
        form = EditProfileModelForm(instance=request.user)

        args = {'form': form}
        return render(request, 'home/edit_profile.html', args)

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/home/account/')
        else:

            args = {'form': form}
            return render(request, 'home/change_password.html', args)

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'home/change_password.html', args)
