from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views
urlpatterns = [
    path(r'', views.home),
    path('admin/', admin.site.urls),
    path(r'home/', include('home.urls')),
]
