from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    on_delete = models.CASCADE,

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender = User)


class ContactForm(models.Model):
    Name = models.CharField(max_length= 50)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Message = models.CharField(max_length= 200)
