from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Comment

def default(request):
    return HttpResponse("Hello Django!")

def showbooks(request):
    # return render(request,'yingping.html')
    shorts = Comment.objects.all()
    return render(request,'yingping.html',locals())