from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

from django.conf import settings
# tus urlpatterns de toda la vida


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'faceschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'template_name': 'logged_out.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
)


urlpatterns += patterns('',
	(r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
        'django.views.static.serve',
        {'document_root' : settings.STATIC_ROOT }),)
