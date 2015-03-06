from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

from django.conf import settings
# tus urlpatterns de toda la vida


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'faceschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^$', views.index, name='index'),
)


urlpatterns += patterns('',
	(r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
        'django.views.static.serve',
        {'document_root' : settings.STATIC_ROOT }),)
