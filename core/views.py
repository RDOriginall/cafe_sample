from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def core_page(request):
    return HttpResponse("Hello this is core page!")