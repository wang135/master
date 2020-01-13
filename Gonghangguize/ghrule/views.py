from django.shortcuts import render

# Create your views here.
import json
import pandas as pd
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView

from ghrule.renhang import People
from ghrule.forms import PeopleinfoModelSerializer

import logging
logger = logging.getLogger('django')
class gonghangrule(APIView):
    print("kaishi")
    # 定义请求方法为post，
    def post(self, request):

        parameter_json = request.body

        # json转字典
        parameter = json.loads(parameter_json)
        print(parameter)
        # 定义请求里的key
        full_name = 'full_name'
        id_no = 'id_no'
        cellphone = 'cellphone'
        id_type = 'id_type'
        ret = {"code":'1000'}
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        try:
            if full_name in parameter and id_no in parameter and cellphone in parameter and id_type in parameter:
                #print('sss',parameter)
                # 取出其request.json中的phone和password
                names = parameter[full_name]
                ids = parameter[id_no]
                phone = parameter[cellphone]
                id_type = parameter[id_type]
                id_type = id_type
                pub_ser = PeopleinfoModelSerializer(data=request.data)
                logger.info("hellll")
                print('pub_ser', pub_ser)
                if pub_ser.is_valid():
                    # print(pub_ser.validated_data)
                    pub_ser.save()
                ## gonghang
                People_renhang = People(names,ids,phone,id_type)
                code = People_renhang.renhanhgomngshang()
                ret = {"code": code}
                return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
        except:
            ret = {"code":'5000'}
            return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
