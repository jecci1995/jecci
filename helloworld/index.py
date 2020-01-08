# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from helloworld.view import check_login

def login(request):
    return render(request, "login.html")

@check_login
def index(request):
    return render(request, "index.html")
@check_login
def index_body(request):
    return render(request, "index-body.html")
@check_login
def task_console_list(request):
    return render(request, "task-console-list.html")
@check_login
def task_console_add(request):
    return render(request, "task-console-add.html")
@check_login
def task_console_con(request):
    return render(request, "task-console-con.html")


@check_login
def user_console_add(request):
    return render(request, "user-console-add.html")
@check_login
def user_console_list(request):
    return render(request, "user-console-list.html")

@check_login
def demo_console(request):
    return render(request, "demo-console.html")
@check_login
def demo_console_history(request):
    return render(request, "demo-console-history.html")
@check_login
def demo_console_add(request):
    return render(request, "demo-console-add.html")
