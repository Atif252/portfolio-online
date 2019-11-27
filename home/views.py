from django.shortcuts import render
from django.http import HttpResponse



def home_screen_view(request):
    return HttpResponse("HERE's some random text for testing my web")