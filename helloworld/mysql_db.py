# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from TestModel.models import Task,Test,User,Democtl,Demostate
from django.http import HttpResponse
from django.contrib import messages



def task_form_action(request):
    ctx = {}
    if request.POST:
        ctx['tnum'] = request.POST['tnum']
        ctx['tjob'] = request.POST['tjob']
        ctx['tgit'] = request.POST['tgit']

    return render(request, "index.html", ctx)



def taskdb(request):
    ctx = {}
    if request.POST:
        ctx['tnum'] = request.POST['tnum']
        ctx['tjob'] = request.POST['tjob']
        ctx['tgit'] = request.POST['tgit']
    query_set = Task.objects.filter(tnum=ctx['tnum'])
    if query_set.exists():
        messages.success(request, "ERROR!任务名程已存在!")
        return render(request, "task-console-add.html")
    crtdb = Task(tnum=ctx['tnum'],tjob=ctx['tjob'],tgit=ctx['tgit'])
    crtdb.save()
    messages.success(request, "数据添加成功!")

    return render(request, "task-console-add.html")

def tasklist(request):
    response = Task.objects.all()
    return render(request, "task-console-list.html", {'res':response})


def useradddb(request):
    ctx = {}
    if request.POST:
        ctx['uname'] = request.POST['uname']
        ctx['supassword'] = request.POST['supassword']
        ctx['note'] = request.POST['note']
    query_set = User.objects.filter(username=ctx['uname'])
    if query_set.exists():
        messages.success(request, "ERROR!用户名已存在!")
        return render(request, "user-console-add.html")
    crtdb = User(username=ctx['uname'],password=ctx['supassword'],note=ctx['note'])
    crtdb.save()
    messages.success(request, "用户添加成功!")

    return render(request, "user-console-add.html")

def userlist(request):
    response = User.objects.all()
    return render(request, "user-console-list.html", {'res':response})

def userdelaction(request):
    ctx = {}
    if request.POST:
        ctx['user_id'] = request.POST['user_id']
    response = User.objects.get(username=ctx['user_id'])
    response.delete()
    messages.success(request, "用户删除成功!")
    return render(request, "user-console-list.html")

def taskdelaction(request):
    ctx = {}
    if request.POST:
        ctx['task_id'] = request.POST['task_id']
    response = Task.objects.get(tnum=ctx['task_id'])
    response.delete()
    messages.success(request, "数据删除成功!")
    return render(request, "task-console-list.html")

def democtllist(request):
    response = Democtl.objects.all()
    return render(request, "demo-console.html", {'res':response})

def demostelist(request):
    response = Demostate.objects.all()
    return render(request, "demo-console-history.html", {'res':response})

def democtladddb(request):
    ctx = {}
    if request.POST:
        ctx['demoname'] = request.POST['demoname']
        ctx['demoattr'] = request.POST['demoattr']
        ctx['democmdname'] = request.POST['democmdname']
        ctx['demohost'] = request.POST['demohost']
        ctx['demoport'] = request.POST['demoport']
        ctx['demostate'] = request.POST['demostate']
        ctx['clist'] = request.POST['clist']
        if ctx['clist'] == '1':
            dbname = Democtl
            crtdb = dbname(demoname=ctx['demoname'], demoattr=ctx['demoattr'], democmdname=ctx['democmdname'],demohost=ctx['demohost'], demoport=ctx['demoport'], demostate=ctx['demostate'])
            msg = '已添加到程序控制表!请联系管理员配置服务控制脚本!'
        elif ctx['clist'] == '2':
            dbname = Demostate
            crtdb = dbname(demoname=ctx['demoname'], demoattr=ctx['demoattr'],demohost=ctx['demohost'], demoport=ctx['demoport'], demostate=ctx['demostate'])
            msg = '已添加到程序状态表!'
        query_set = dbname.objects.filter(demoname=ctx['demoname'])
        if query_set.exists():
            messages.success(request, "ERROR!程序名称已存在!")
            return render(request, "demo-console-add.html")
        crtdb.save()
        messages.success(request, msg)
        return render(request, "demo-console-add.html")
    return render(request, "demo-console-add.html")

def democtldelaction(request):
    ctx = {}
    if request.POST:
        ctx['demo_id'] = request.POST['demo_id']
    response = Democtl.objects.get(demoname=ctx['demo_id'])
    response.delete()
    messages.success(request, "数据删除成功!")
    return render(request, "demo-console.html")
