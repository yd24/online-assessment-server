from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def hello_world(request):
    return HttpResponse('hello world')

