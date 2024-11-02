from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('', include('sistema_de_login.urls')),
    path('api/', api.urls, name='docs'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
