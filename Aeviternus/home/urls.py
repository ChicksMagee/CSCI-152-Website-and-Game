from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^buy-now/$', views.buyNow, name='buy-now'),
    url(r'^buy-form/$', views.buyForm, name='buy-form'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home/logout.html'}, name='logout'),
    url(r'^account/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^account/$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/password/$', views.change_password, name='change_password'),
]
