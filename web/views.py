from django.shortcuts import render
from django.http import HttpResponse
from forms import newPostForm
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
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
	
	if request.method == 'POST':
		
		form=newPostForm(request.POST, request.FILES)

		if form.is_valid():
		
			form_save=form.save()		
					
	posts=Post.objects.filter(channel__in=channel_id)
	posts=posts.order_by('-pub_date')
	form_post=newPostForm(initial={'channel':channel_id,'user':request.user.fsuser})
	likes=Like.objects.all()
	return render( request, 'posts.html', {"posts": posts,"form_post":form_post,"likes":likes} )

@csrf_exempt

def LikePost(request):
    #TEST $ curl localhost:8000/web/like/ -d '{"a":1}'

    if request.method=='POST':

    	new_like=Like()
    	new_like.postID=request.POST.get('postID')
    	new_like.user=request.user.fsuser

    	new_like_save=new_like.save()


			


def LTPosts(request):
	return render (request, 'latest_posts.html')

