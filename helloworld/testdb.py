# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
    response = ''
    response1 = ''
    #test1 = Test.objects.get(id=1)
    #test1.name = 'wohencai'
    #test1.save()
    #通过objects 这个模型管理器的all()活动所有数据行，相当于sql里的select * from
    list = Test.objects.all()
    Test.objects.filter(id=2).update(name='jcl')
    

    #filter相当于sql中的where,可设置条件过滤结果
    #response2 = Test.objects.filter(id=1)

    #获取单个对象
    #response3 = Test.objects.get(id=1)

    #限制返回的数据，相当于offset 0 limit 2
    #Test.objects.order_by('name')[0:2]

    #Test.objects.filter(name="runoob").order_by("id")
    #for var in list:
     #   response1 += var.name + ""
    #response = response1
    #return HttpResponse("<p>" esponse "</p>")
    for var in list:
        response1 += var.name + ""
    response = response1
    return HttpResponse("<p> 修改成功 </p>" + "<p>" + response + "</p>")
    
    #数据排序
    #Test.objects.order_by("id")
    #test1 = Test(name='runoob')
    #test1.save()
    #return HttpResponse("<p>数据添加成功！</p>")
