from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def hand404(request, exception):
    return render(request, '404.html', status=404)