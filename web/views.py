from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from forms import newPostForm
from models import *
from models import Post
from django.shortcuts import render_to_response
from forms import PostForm, BadwForm, GoodwForm, RemovebadwForm, RemovegoodwForm, BadwmasivaForm, GoodwmasivaForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.mail import send_mail 
from web.models import Badws, Goodws, Removebadws, Removegoodws, Badwsmasiva, Goodwsmasiva
from word_filter import language_filter
from masive_filter import bmasive_upload_filter
from masive_filter import gmasive_upload_filter
from remove_filter import gremove_filter 
from remove_filter import bremove_filter
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    channels=Channel.objects.filter(users__in=[request.user.fsuser])
    return render( request, 'main.html', {"latest_posts": latest_posts, "canals_subs":channels})

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

	comments=''
	form_post=newPostForm()
	return render( request, 'posts.html', {"posts": posts,"form_post":form_post,"comment":comments} )

def LTPosts(request):
	return render (request, 'latest_posts.html')

def crear(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']   
	    message = str(message).encode('utf-8')
	    if (language_filter(message)=="no"):
		message = "Don't publish"
                return HttpResponseRedirect('/web/filtererror')
	    else:
	        form.save()

            return HttpResponseRedirect('/web')
    else:
        form = PostForm()
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('crear_articulo.html', args)



def badw(request):
    if request.POST:
        form = BadwForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['texto']
            form.save()
            return HttpResponseRedirect('/web/badwlist')
    else:
        form = BadwForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('badw.html', args)

def goodw(request):
    if request.POST:
        form = GoodwForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['texto']
	    form.save()
            return HttpResponseRedirect('/web/goodwlist')
    else:
        form = GoodwForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('goodw.html', args)

def badwlist(request):
    entradas = Badws.objects.all()[:50]
    return render_to_response('badwlist.html', {'badws' : entradas})

def goodwlist(request):
    entradas = Goodws.objects.all()[:50]
    return render_to_response('goodwlist.html', {'goodws' : entradas})

def badwmasiva(request):
    if request.POST:
        form = BadwmasivaForm(request.POST,request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            bmasive_upload_filter(archivo)
            form.save()
            return HttpResponseRedirect('/web/badwlist')
    else:
        form = BadwmasivaForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('badwmasiva.html', args)

def goodwmasiva(request):
    if request.POST:
        form = GoodwmasivaForm(request.POST,request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
	    gmasive_upload_filter(archivo)
            form.save()
            return HttpResponseRedirect('/web/goodwlist')
    else:
        form = GoodwmasivaForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('goodwmasiva.html', args)

def removegoodw(request):
    if request.POST:
        form = RemovegoodwForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['texto']
            gremove_filter(message)
            return HttpResponseRedirect('/web/goodwlist')
    else:
        form = RemovegoodwForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('removegoodw.html', args)

def removebadw(request):
    if request.POST:
        form = RemovebadwForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['texto']
	    bremove_filter(message)
            return HttpResponseRedirect('/web/badwlist')
    else:
        form = RemovebadwForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form 
    return render_to_response('removebadw.html', args)

def filtererror(request):
    return render_to_response('filtererror.html')
