from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from home.models import ContactForm, UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ContactModelForm(ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(max_length=50, required=False)

    class Meta:
        model = ContactForm
        fields = ['name','email','phone','message']

class EditProfileModelForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
