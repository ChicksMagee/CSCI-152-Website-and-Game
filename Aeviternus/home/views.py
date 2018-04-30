from django.shortcuts import render, redirect
from home.forms import RegistrationForm, ContactModelForm

def home(request):
    return render(request, 'home/home.html')

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
            return render(request, 'home/register.html', args)
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
