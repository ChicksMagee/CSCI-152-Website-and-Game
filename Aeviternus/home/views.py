from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def buyNow(request):
    return render(request, 'home/buy-now.html')

def contact(request):
    return render(request, 'home/contact.html')
