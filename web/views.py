from django.shortcuts import render
from django.http import HttpResponse

def index( request ):
    return HttpResponse("Welcome to Faceschool")

def post_detail( request, post_id ):
    return HttpResponse("Post detail...")
