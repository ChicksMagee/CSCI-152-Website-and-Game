from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name =  models.CharField(max_length=25, default='')
    last_name =  models.CharField(max_length=25, default='')
    email = models.EmailField(default='')
    phone = models.IntegerField(default='')
    description = models.CharField(max_length=500, default='')
    street_address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    zipcode = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='profile_image', blank=True)
    on_delete = models.CASCADE

    def __str__(self):
        title = self.first_name + " " + self.last_name + "'s User Profile"
        return title

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender = User)


class ContactForm(models.Model):
    name = models.CharField(max_length= 25, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length= 10, default='')
    message = models.CharField(max_length= 500, default='')

    def __str__(self):
        title = self.name + "'s Contact Form"
        return title
