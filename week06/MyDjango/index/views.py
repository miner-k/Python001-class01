from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

from .models import Name


def index(request):
    return HttpResponse("Hello Django!")

def year(request,year):
    return HttpResponse(year)
def printstr(request,**str1):
    return HttpResponse(str1['str1'])

def myyear(request,year):
    return render(request,'yearview.html')

def myredicet(request,year):
    return  redirect('/2020.html')

def show_books(request):
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())
