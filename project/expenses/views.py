from django.shortcuts import render
from django.http import HttpResponse
from expenses.models import Summary, Detail

def index(request): # index takes 'request' as an argument #describes the request being passed # request object contains MANY different types of attributes
  total = Summary.objects.count()

  return HttpResponse(f"Hello, world. You're at the expenses index and we have some {total} of summery objects.")

# Create your views here.
