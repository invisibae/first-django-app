from django.shortcuts import render
from django.http import HttpResponse

def index(request): # index takes 'request' as an argument #describes the request being passed # request object contains MANY different types of attributes
  return HttpResponse("Hello, world. You're at the expenses index.")

# Create your views here.
