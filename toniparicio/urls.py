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
    path('admin/', admin.site.urls),                                            # admin routes
    url(r'^', include('apps.blog.urls')),                                       # apps routes
    url(r'^summernote/', include('django_summernote.urls')),                    # text editor routes
    url(r'^api/$', get_swagger_view(title='Toni Paricio API')),                 # API docs routes
    url(r'^api/(?P<version>(v1|v2))/', include('apps.quotes.urls')),            # API routes
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),   # oauth routes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)               # static routes
