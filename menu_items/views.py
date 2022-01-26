from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def menu_item_page(request):
    return HttpResponse("Hello this is Menu item page!")