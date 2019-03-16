from django.shortcuts import render
from django.http import HttpResponse

from .scripts import hello

# Create your views here.
def printHello(request):
    if request.method == "GET":
        pass

    return HttpResponse(hello.printHello())
    # return HttpResponse('<h1>Hello World!</h1>')
