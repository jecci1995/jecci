import os
import telnetlib
from TestModel.models import Democtl,Demostate

def socron():
    response = []
    list = Democtl.objects.all()
    for var in list:
        res = {}
        res['demoname']=var.demoname
        res['demohost']=var.demohost
        res['demoport']=var.demoport
        response.append(res)
    state_run = '运行中'
    state_stop = '未运行'
    section_list = response

    for sc in section_list:
        DemoName = sc['demoname']
        HostIP = sc['demohost']
        DemoPort = sc['demoport']
        try:
            tel = telnetlib.Telnet(HostIP, port=DemoPort, timeout=3)
            tel.close()
            writeTodb( DemoName, HostIP, DemoPort, state_run)
        except:
            writeTodb(DemoName, HostIP, DemoPort, state_stop)

    response2 = []
    list2 = Demostate.objects.all()
    for var2 in list2:
        res2 = {}
        res2['demoname'] = var2.demoname
        res2['demohost'] = var2.demohost
        res2['demoport'] = var2.demoport
        response2.append(res2)
    section_list2 = response2
    for sc in section_list2:
        DemoName = sc['demoname']
        HostIP = sc['demohost']
        DemoPort = sc['demoport']
        try:
            tel = telnetlib.Telnet(HostIP, port=DemoPort, timeout=3)
            tel.close()
            writeTodb2( DemoName, HostIP, DemoPort, state_run)
        except:
            writeTodb2(DemoName, HostIP, DemoPort, state_stop)
def writeTodb(DemoName, HostIP, DemoPort, status):
    #print(DemoName, HostIP, DemoPort, status)
    changedb = Democtl.objects.get(demoname=DemoName,demohost=HostIP,demoport=DemoPort)
    changedb.demostate = status
    changedb.save()
def writeTodb2(DemoName, HostIP, DemoPort, status):
    print(DemoName, HostIP, DemoPort, status)
    changedb = Demostate.objects.get(demoname=DemoName,demohost=HostIP,demoport=DemoPort)
    changedb.demostate = status
    changedb.save()

