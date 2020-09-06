from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment20200904
from .models import Pid8F332Caa60
import time

brands_dic = {
    "PHILIPS": 0,
    "MI": 0,
    "SONY": 0,
    "HUAWEI": 0,
    "Haier": 0,
    "Apple": 0,
    "SAMSUNG": 0,
    "Lenovo": 0,
    "HP": 0,
    "ASUS": 0,
    "Hisense": 0,
    "TCL": 0,
    "HONOR": 0,
    "KONKA": 0,
    "GREE": 0,
    "CHANGHONG": 0,
    "YOUPIN": 0,
    "LG": 0,
    "Redmi": 0,
    "MEIZU": 0,
    "RAZER": 0,
    "Microsoft": 0,
    "Hasee": 0,
    "360": 0,
    "OPPO": 0,
    "vivo": 0,
    "BenQ": 0,
    "SHARP": 0,
    "ZMI": 0,
    "ROG": 0,
    "other": 0,
}



def index(request):
    # return HttpResponse("Hello Django!")
    return render(request,'index.html')


def show_today(request):
    n = Comment20200904.objects.all()
    now_day = time.strftime("%Y-%m-%d", time.localtime())
    count = len(n)
    comment_sum = 0
    phone_count_max = 0
    for phone in n:
        comment_sum += int(phone.comment_count)

        for key in brands_dic.keys():
            if phone.product_name.find(key) > 0 :
                brands_dic[key] += 1
                break
        else:
            brands_dic['other'] += 1

    tmp = brands_dic.copy()
    for key,value in tmp.items():
        if value == 0:
            brands_dic.pop(key)
            continue
        if value > phone_count_max:
            phone_count_max = value
    # print(phone_count_max,brands_dic)
    barnds_list  = list(brands_dic.keys())
    barnds_count_list  = list(brands_dic.values())

    return render(request,'dayshow.html',locals())


def show_product(request):

    product_comments = Pid8F332Caa60.objects.all()
    negative_count = 0
    positive_count = 0
    for product_comment in  product_comments:
        if float(product_comment.emotional_value) >= 0.5 :
            positive_count += 1
        else:
            negative_count += 1
    positive_proportion = (round(positive_count /(positive_count + negative_count) * 100))
    count = len(product_comments)
    return render(request,'productshow.html',locals())