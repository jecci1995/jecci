# -*-8 coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_from(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的你内容是：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)