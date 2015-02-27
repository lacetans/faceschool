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

]
