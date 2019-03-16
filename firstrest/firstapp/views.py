from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def printHello(request):
    if request.method == "GET":
        pass

    return HttpResponse('<h1>Hello World!</h1>')
