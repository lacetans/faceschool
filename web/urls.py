from django.conf.urls import patterns,include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='detail'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^channels/$',views.ShowChannels, name="channels"),
    url(r'^channel/(?P<channel_id>[0-9]+)/$',views.ShowPosts,name="posts"),
    url(r'^posts/$',views.LTPosts, name="posts"),
    url(r'^like_post/$',views.LikePost, name="like_post"),
    url(r'^crear/', 'web.views.crear', name='crear'),
    url(r'^badw/', 'web.views.badw', name='badw'),
    url(r'^goodw/', 'web.views.goodw', name='goodw'),
    url(r'^removebadw/', 'web.views.removebadw', name='removebadw'),
    url(r'^removegoodw/', 'web.views.removegoodw', name='removegoodw'),
    url(r'^badwlist/', 'web.views.badwlist', name='badwlist'),
    url(r'^goodwlist/', 'web.views.goodwlist', name='goodwlist'),
    url(r'^badwmasiva/', 'web.views.badwmasiva', name='badwmasiva'),
    url(r'^goodwmasiva/', 'web.views.goodwmasiva', name='goodwmasiva'),
    url(r'^filtererror/', 'web.views.filtererror', name='filtererror'),
]
