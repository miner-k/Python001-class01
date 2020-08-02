from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.http import HttpResponse


def showBook(request):
    return HttpResponse("Hello Django!")