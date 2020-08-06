from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

from .models import Name
from .models import T1
from django.db.models import Avg

def default(request):
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

def index(request):
    n = T1.objects.all()
    count = n.count()

    # 平均星级
    star_avg =f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"

    # 情感倾向
    sent_avg =f"{T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数据
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    print('star_avg：' + sent_avg + "  sent_avg:" + sent_avg)
    return render(request,'index.html',locals())

def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
