from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', items, name='items'),
    url(r'^categories/$', categories, name='categories')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
