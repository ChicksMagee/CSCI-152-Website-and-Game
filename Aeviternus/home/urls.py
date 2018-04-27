from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^buy-now/$', views.buyNow, name='buy-now'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
