from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^crear/', 'web.views.crear', name='crear'),
    url(r'^badw/', 'web.views.badw', name='badw'),
    url(r'^goodw/', 'web.views.goodw', name='goodw'),
    url(r'^removebadw/', 'web.views.removebadw', name='removebadw'),
    url(r'^removegoodw/', 'web.views.removegoodw', name='removegoodw'),
    url(r'^badwlist/', 'web.views.badwlist', name='badwlist'),
    url(r'^goodwlist/', 'web.views.goodwlist', name='goodwlist'),
    url(r'^badwmasiva/', 'web.views.badwmasiva', name='badwmasiva'),
    url(r'^goodwmasiva/', 'web.views.goodwmasiva', name='goodwmasiva'),
]
