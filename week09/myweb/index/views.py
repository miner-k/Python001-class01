from django.shortcuts import render,HttpResponse

# Create your views here.

from .form import LoginForm,SigninForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User
def login(request):

    if request.method == 'GET':
        login_form = LoginForm()
        return  render(request,'form2.html',{'form': login_form})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password']) # 从数据库中查询该用户是否存在，如果不存在返回空
            if user:
                # 登陆用户
                # login(request, user)
                return HttpResponse('登录成功')
            else:
                # return HttpResponse('登录失败')
                outline = '登录失败'
                return render(request,'loginout.html',{'outline': outline})

def signin(request):

    if request.method == 'GET':
        login_form = SigninForm()
        return  render(request,'signin.html',{'form': login_form})

    if request.method == 'POST':
        login_form = SigninForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password']) # 从数据库中查询该用户是否存在，如果不存在返回空
            if user:

                return HttpResponse('已经存在')
            else:
                user = User.objects.create_superuser(cd['username'],cd['email'],cd['password'])
                user.save()

                return  render(request,'signinout.html',{'form': '注册成功'})
                # return HttpResponse('注册成功')