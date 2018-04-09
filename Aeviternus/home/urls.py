from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^buy-now/$', views.buyNow, name='buy-now'),
    url(r'^login/$', views.login, name='login'),
]
