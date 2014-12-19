from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='detail'),
]
