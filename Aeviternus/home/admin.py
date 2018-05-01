from django.contrib import admin
from home.models import UserProfile, ContactForm, Post

admin.site.register(UserProfile)
admin.site.register(ContactForm)
admin.site.register(Post)
