from django.shortcuts import render
from django.http import HttpResponse

from models import Post

def index( request ):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    return render( request, 'base.html', {"latest_posts": latest_posts} )

def post_detail( request, post_id ):
    return HttpResponse("Post detail...")
