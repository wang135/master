from django.shortcuts import render
import time
# Create your views here.
import json
import pandas as pd
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView

#from ghrule.renhang import People
from ghrule.forms import PeopleinfoModelSerializer
from ghrule.renhang import People

import Gonghangguize.settingss as settings

from Emailsend.send import  SendMail
import logging
logger = logging.getLogger('django')

## 自动发邮件邮箱的设置
username=settings.username
passwd=settings.passwd
recv=settings.recv
title=settings.title
content=settings.content
file= settings.file
ssl=settings.ssl

mail = SendMail(
        username,
        passwd,
        recv,
        title,
        content,
        file,
        ssl,
    )
a = time.clock()
logger.info("开始时间",a)

class gonghangrule(APIView):
    # 定义请求方法为post，
    def post(self, request):

        parameter_json = request.body

        # json转字典
        parameter = json.loads(parameter_json)
        #print(parameter)
        logger.info(parameter)
        # 定义请求里的key
        full_name = 'full_name'
        id_no = 'id_no'
        #cellphone = 'cellphone'
        id_type = 'id_type'
        ret = {"code":'1000'}
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        try:
            if full_name in parameter and id_no in parameter and  id_type in parameter:
                #print('sss',parameter)
                # 取出其request.json中的phone和password
                names = parameter[full_name]
                ids = parameter[id_no]

                id_type = parameter[id_type]
                id_type = id_type

                pub_ser = PeopleinfoModelSerializer(data=request.data)
                logger.info("hellll")
                #print('pub_serpub_serpub_serpub_ser',pub_ser)
                # if pub_ser.is_valid():
                #     pub_ser.save()
                if pub_ser.is_valid():
                    n = 0
                    while n <5:
                        try:
                            pub_ser.save()
                            break
                        except:
                            n+=1



                ## gonghang
                People_renhang = People(names,ids,id_type)
                code = People_renhang.renhanhgomngshang()
                logger.info(code)
                #mail.send_mail()
                ret = {"code": code}
                #mail.send_mail()
                d= time.clock()
                logger.info("结束时间时间",d )
                return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
        except:
            ret = {"code":'5000'}
            logger.info("错误的信息",ret)
            mail.send_mail()
            return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")

class yunwei(APIView):
    def get(self, request):
        a = '20000'
        return HttpResponse(a)




