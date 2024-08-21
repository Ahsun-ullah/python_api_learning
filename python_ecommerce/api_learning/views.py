from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def api_learning(req):
    return HttpResponse('<h1>Congratulations..!Your api working fine.</h1>')