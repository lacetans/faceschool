from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'faceschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^', include('web.urls')),
    url(r'^$', views.index, name='index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
