from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from forms import newPostForm
from models import *

def index( request ):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    return render( request, 'base.html', {"latest_posts": latest_posts} )

def post_detail( request, post_id ):
    return HttpResponse("Post detail...")

@login_required
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

	comments=''
	form_post=newPostForm()
	return render( request, 'posts.html', {"posts": posts,"form_post":form_post,"comment":comments} )

def LTPosts(request):
	return render (request, 'latest_posts.html')

