from django.shortcuts import render
from django.http import HttpResponse

from models import *

def index( request ):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    return render( request, 'base.html', {"latest_posts": latest_posts} )

def post_detail( request, post_id ):
    return HttpResponse("Post detail...")

def ShowChannels(request):
	channels=Channel.objects.filter(users__in=[request.user.fsuser])
	return render (request, 'canals.html', {"canals_subs":channels})

def ShowPosts(request, channel_id):
	
	posts=Post.objects.filter(channel__in=channel_id)
	posts=posts.order_by('-pub_date')
	return render( request, 'posts.html', {"posts": posts} )
