from django.test import TestCase
from django.urls import resolve, reverse
from home.forms import RegistrationForm, ContactModelForm, EditProfileModelForm


class MyFormTests(TestCase):
    def test_registration_form_is_valid(self):
        form_data = {'username': 'tesamra',
        'first_name': 'Troy',
        'last_name': 'Samra',
        'email': 'tesamra@gmail.com',
        'password1': 'samra121193',
        'password2': 'samra121193'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_is_not_valid_no_first_and_last_name(self):
        form_data = {'username': 'tesamra',
        'first_name': '',
        'last_name': '',
        'email': 'tesamra@gmail.com',
        'password1': 'samra',
        'password2': 'samra121193'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_not_valid_blank_username(self):
        form_data = {'username': '',
        'first_name': 'Troy',
        'last_name': 'Samra',
        'email': 'tesamra@gmail.com',
        'password1': 'samra121193',
        'password2': 'samra121193'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_not_valid_no_password_match(self):
        form_data = {'username': 'tesamra',
        'first_name': 'Troy',
        'last_name': 'Samra',
        'email': 'tesamra@gmail.com',
        'password1': 'samra',
        'password2': 'samra121193'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registration_form_is_not_valid_wrong_email(self):
        form_data = {'username': 'tesamra',
        'first_name': 'Troy',
        'last_name': 'Samra',
        'email': 'gmail.com',
        'password1': 'samra121193',
        'password2': 'samra121193'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_model_form_is_valid(self):
        form_data = {'name': 'Troy Samra',
        'email': 'tesamra@gmail.com',
        'phone': '5593416905',
        'message':'Hello World'}
        form = ContactModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_model_form_is_valid_no_message(self):
        form_data = {'name': 'Troy Samra',
        'email': 'tesamra@gmail.com',
        'phone': '5593416905',
        'message':''}
        form = ContactModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_model_form_is_not_valid_blank_name(self):
        form_data = {'name': '',
        'email': 'tesamra@gmail.com',
        'phone': '5593416905',
        'message':'Hello World'}
        form = ContactModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_model_form_is_not_valid_wrong_email(self):
        form_data = {'name': 'Troy Samra',
        'email': 'tesamra@gma',
        'phone': '5593416905',
        'message':'Hello World'}
        form = ContactModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_contact_model_form_is_not_valid_wrong_phone(self):
        form_data = {'name': '',
        'email': 'tesamra@gmail.com',
        'phone': 'fdsfsdfsdf',
        'message':'Hello World'}
        form = ContactModelForm(data=form_data)
        self.assertFalse(form.is_valid())

class MyUrlTests(TestCase):
    def test_home_url_is_valid(self):
        url = reverse('home')
        self.assertEqual(url, '/home/')

    def test_about_url_is_valid(self):
        url = reverse('about')
        self.assertEqual(url, '/home/about/')

    def test_buy_now_url_is_valid(self):
        url = reverse('buy-now')
        self.assertEqual(url, '/home/buy-now/')

    def test_contact_url_is_valid(self):
        url = reverse('contact')
        self.assertEqual(url, '/home/contact/')

    def test_login_url_is_valid(self):
        url = reverse('login')
        self.assertEqual(url, '/home/login/')

    def test_register_url_is_valid(self):
        url = reverse('register')
        self.assertEqual(url, '/home/register/')

    def test_logout_url_is_valid(self):
        url = reverse('logout')
        self.assertEqual(url, '/home/logout/')

    def test_account_url_is_valid(self):
        url = reverse('account')
        self.assertEqual(url, '/home/account/')

    def test_change_password_url_is_valid(self):
        url = reverse('change_password')
        self.assertEqual(url, '/home/account/password/')

    def test_edit_profile_url_is_valid(self):
        url = reverse('edit_profile')
        self.assertEqual(url, '/home/account/edit/')

    def test_buy_form_url_is_valid(self):
        url = reverse('buy-form')
        self.assertEqual(url, '/home/buy-form/')

class MyViewTests(TestCase):
    def test_call_view_loads(self):
        self.client.login(username='tesamra', password='samra121193')
        response = self.client.get('/home/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/account.html')

    def test_view_fails_blank(self):
        self.client.login(username='tesamra', password='samra121193')
        response = self.client.post('/home/contact/', {}) # blank data dictionary
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        # etc. ...

    def test_view_fails_invalid(self):
        self.client.login(username='tesamra', password='samra121193')
        response = self.client.post('/home/contact/', {'email': '213213'}) # invalid input
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_view_suceeds(self):
        self.client.login(username='tesamra', password='samra121193')
        response = self.client.post('/home/contact/', {'name': 'Troy Samra',
        'email': 'tesamra@gmail.com',
        'phone': '5593416905',
        'message':'Hello World'})
        self.assertRedirects(response, '/')
