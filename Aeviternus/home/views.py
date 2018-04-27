from django.shortcuts import render, redirect
from home.forms import RegistrationForm, ContactForm

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def buyNow(request):
    return render(request, 'home/buy-now.html')

def contact(request):
    print("Hello form is Submitted.")
    Name = request.POST['name']
    Email = request.POST["email"]
    Phone = request.POST["phone"]
    Message = request.POST["message"]

    ContactForm = ContactForm(Name= name, Email=email, Phone=phone, Message=message)

    ContactForm.save()

    return render(request, 'home/contact.html')

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'home/reg_form.html', args)

def get(self, request):
    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def post(self, request):
    form = ContactForm(request.POST)
    if form.is_valid():
        Name = form.cleaned_data['Name']
        Email = form.cleaned_data['Email']
        Phone = form.cleaned_data['Phone']
        Message = form.cleaned_data['Message']

        args = {'form': form, 'Name': Name, 'Email':Email, 'Phone':Phone, 'Message':Message}

        return render(request, 'home/contact.html', args)
