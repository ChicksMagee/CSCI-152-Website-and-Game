from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'', views.home),
    path('admin/', admin.site.urls),
    path(r'home/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
