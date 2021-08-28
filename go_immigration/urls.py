"""go_immigration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.views.generic.base import RedirectView

from go_immigration import settings

admin.site.site_header = 'GO IMMIGRATION'
admin.site.site_title = 'go_immigration records'
admin.site.index_title = 'ADMINISTRATION GO IMMIGRATION'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('records.urls')),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                  path(
                      "favicon.ico",
                      RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
                  ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
