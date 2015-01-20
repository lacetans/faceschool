from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'faceschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^crear/', 'web.views.crear', name='crear'),
    url(r'^badw/', 'web.views.badw', name='badw'),
    url(r'^goodw/', 'web.views.goodw', name='goodw'),
    url(r'^removebadw/', 'web.views.removebadw', name='removebadw'),
    url(r'^removegoodw/', 'web.views.removegoodw', name='removegoodw'),
    url(r'^badwlist/', 'web.views.badwlist', name='badwlist'),
    url(r'^goodwlist/', 'web.views.goodwlist', name='goodwlist'),
    url(r'^badwmasiva/', 'web.views.badwmasiva', name='badwmasiva'),
    url(r'^goodwmasiva/', 'web.views.goodwmasiva', name='goodwmasiva'),
)
