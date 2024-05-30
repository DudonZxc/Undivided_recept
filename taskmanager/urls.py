
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from taskmanager import settings
from main.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
    path('accounts/', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
