from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'page/home.html')

def method(request):
    return render(request, 'page/method.html')

def conclusion(request):
    return render(request, 'page/conclusion.html')
