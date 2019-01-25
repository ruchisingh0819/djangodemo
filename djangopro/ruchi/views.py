from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("WELCOME RUCHI")
def index1(request):
    return HttpResponse("helloooo")

