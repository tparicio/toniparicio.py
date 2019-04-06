"""toniparicio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    # admin routes
    path('admin/', admin.site.urls),
    # login routes
    url(r'^', include(('apps.registration.urls', 'apps.registration'), namespace='registration')),
    url(r'^', include(('apps.blog.urls', 'apps.blog'), namespace='blog')),
    # text editor routes
    url(r'^summernote/', include('django_summernote.urls')),
    # API routes
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api/$', get_swagger_view(title='Toni Paricio API')),
    url(r'^api/(?P<version>(v1|v2))/', include('apps.quotes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)               # static routes
