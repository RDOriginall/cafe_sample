from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def orders_page(request):
    return HttpResponse("Hello this is Orders page!")