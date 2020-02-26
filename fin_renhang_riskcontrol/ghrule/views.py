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

# mail =SendMail()

class gonghangrule:
    # 定义请求方法为post，
    def get(self, parameter):
        a = time.clock()
        # logger.info("开始时间{a}".format(a=a))
        # parameter_json = request.body
        #
        # # json转字典
        # parameter = json.loads(parameter_json)
        #print(parameter)
        logger.info(parameter)
        # 定义请求里的key
        full_name = 'full_name'
        id_no = 'id_no'
        #cellphone = 'cellphone'
        id_type = 'id_type'
        ret = {"code":'1000'}
        # data1 = request.data
        # print('qqqqqqqqqqqq',data1)
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        try:
            if full_name in parameter and id_no in parameter and  id_type in parameter:
                #print('sss',parameter)
                # 取出其request.json中的phone和password
                names = parameter[full_name]
                ids = parameter[id_no]

                id_type = parameter[id_type]
                id_type = id_type
                ## gonghang
                b = time.clock()
                logger.info("开始调用时间{b}". format(b=b))
                People_renhang = People(names,ids,id_type)
                code = People_renhang.renhanhgomngshang()
                #print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',code)
                c = time.clock()
                logger.info("调用结束的时间{c}". format(c=c))
                logger.info("调用总共的时间{diff}".format(diff=c-b))
                logger.info(code)
                #mail.send_mail()
                ret = {"code": code}
                #mail.send_mail()

                parameter['code'] = code
                # cntent = names+str(ids)
                # mail = SendMail(content = cntent)
                # mail.send_mail()
                #print('data1',data1)
                pub_ser = PeopleinfoModelSerializer(data=parameter)
                logger.info("hellll")
                # print('pub_serpub_serpub_serpub_ser',pub_ser)
                # if pub_ser.is_valid():
                #     pub_ser.save()

                if pub_ser.is_valid():
                    n = 0
                    while n < 5:
                        try:
                            pub_ser.save()
                            break
                        except:

                            n += 1
                else:
                    pass
                    # print('eeeeeeeeeeeeeeeee', pub_ser.errors)

                d= time.clock()
                logger.info("结束时间时间和获取三方数据时间结束时间{ee}".format(ee=d-c))

                logger.info("结束时间时间{dd}".format(dd = d-a))
                logger.info("三方时间和总时间的比例{ee}".format(ee=(c-b)/(d-a)))
                return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
        except:
            ret = {"code":'5000'}
            logger.info("错误的信息",ret)
            over = time.clock()
            logger.info("错误时候返回来所用时间{over_diff}".format(over_diff=over -a))
            parameter['code'] = code
            names = parameter['full_name']
            ids = parameter['id_no']
            cntent = names + str(ids)
            mail = SendMail(content=cntent)
            mail.send_mail()
            return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")

class yunwei(APIView):
    def get(self, request):
        a = '20000'
        return HttpResponse(a)




