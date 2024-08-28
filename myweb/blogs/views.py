from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def blogs(request):
  template = loader.get_template('blogs.html')
  return HttpResponse(template.render())