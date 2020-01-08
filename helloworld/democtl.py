from django.shortcuts import render
from TestModel.models import Democtl
from django.contrib import messages
import os

def democtl_run_action(request):
    ctx = {}
    if request.POST:
        ctx['demo_id'] = request.POST['demo_id']
        ctx['host_ip'] = request.POST['host_ip']
        query_set = Democtl.objects.filter(demoname=ctx['demo_id'])
        if query_set.exists():
            messages.success(request, "命令已发出,启动程序中...")
            os.system("/python/.sh/democtl.sh %s run %s" % (ctx['demo_id'],ctx['host_ip']))
            return render(request, "demo-console.html")
        else:
            messages.success(request, "ERROR!程序不存在!")
            return render(request, "demo-console.html")
        return render(request, "demo-console.html")
    return render(request, "demo-console.html")
def democtl_stop_action(request):
    ctx = {}
    if request.POST:
        ctx['demo_id'] = request.POST['demo_id']
        ctx['host_ip'] = request.POST['host_ip']
        query_set = Democtl.objects.filter(demoname=ctx['demo_id'])
        if query_set.exists():
            messages.success(request, "命令已发出,停止程序中...")
            os.system("sh /python/.sh/democtl.sh %s stop %s" % (ctx['demo_id'],ctx['host_ip']))
            return render(request, "demo-console.html")
        else:
            messages.success(request, "ERROR!程序不存在!")
            return render(request, "demo-console.html")
        return render(request, "demo-console.html")
    return render(request, "demo-console.html")
def democtl_reload_action(request):
    ctx = {}
    if request.POST:
        ctx['demo_id'] = request.POST['demo_id']
        ctx['host_ip'] = request.POST['host_ip']
        query_set = Democtl.objects.filter(demoname=ctx['demo_id'])
        if query_set.exists():
            messages.success(request, "命令已发出,重启程序中...")
            os.system("/python/.sh/democtl.sh %s reload %s" % (ctx['demo_id'],ctx['host_ip']))
            return render(request, "demo-console.html")
        else:
            messages.success(request, "ERROR!程序不存在!")
            return render(request, "demo-console.html")
        return render(request, "demo-console.html")
    return render(request, "demo-console.html")
