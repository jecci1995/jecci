from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from TestModel.models import User
from functools import wraps
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('login.html')
    return inner

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username,password=password)
        print(user)
        if user:
            request.session['is_login']='1'
            request.session['user_id'] = user[0].id
            return redirect('../index.html')
        return render(request, 'login.html')

@check_login
def hello(request):
    # students=Students.objects.all()  ## 说明，objects.all()返回的是二维表，即一个列表，里面包含多个元组
    # return render(request,'index.html',{"students_list":students})
    # username1=request.session.get('username')
    user_id1 = request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj = User.objects.filter(id=user_id1)
    userobj
    if userobj:
        return render(request, 'index.html', {"user": userobj[0]})
    else:
        return render(request, 'index.html',{"user":'匿名用户'})
