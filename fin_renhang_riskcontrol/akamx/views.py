from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.views import APIView
from  rest_framework import viewsets
from  rest_framework.request import Request
from  rest_framework.authentication import BasicAuthentication

from akamx.models import Peopleinfo,jsonss

from  rest_framework import exceptions

from rest_framework.permissions import BasePermission


import io
from rest_framework.parsers import JSONParser
### 新增加了
import time, datetime
from Emailsend.send import  SendMail
from akamx.forms import PeopleinfoModelSerializer,jsonssModelSerializer
import json
import pandas as pd
from django.shortcuts import render,HttpResponse
from akamx.bairong import Bairong
import json
from bs4 import BeautifulSoup
import requests
from akamx.lujing import lujings
from akamx.tongdun import Tongdun
from akamx.ir import Score
from rest_framework.response import Response
from akamx.bairongcelv import sanfang
from akamx.pboccl import People
from akamx.models import jsonss
score = Score()
lujins = lujings()
www = lujins.shenfen()

import logging
logger = logging.getLogger('django')
class akmoxing(APIView):
    ##print("kaishi")
    # 定义请求方法为post，
    def post(self, request):
        a = time.clock()
        logger.info("开始时间{a}".format(a=a))
        parameter_json = request.body

        # json转字典
        parameter = json.loads(parameter_json)
        ##print(parameter)
        # 定义请求里的key
        full_name = 'full_name'
        id_no = 'id_no'
        cellphone = 'cellphone'
        id_type = 'id_type'
        money = 'money'
        ret = {"code":'1000'}
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        try:
            if full_name in parameter and id_no in parameter and cellphone in parameter and id_type in parameter:
                ##print('sss',parameter)
                # 取出其request.json中的phone和password
                names = parameter[full_name]
                ids = parameter[id_no]
                phone = parameter[cellphone]
                money = parameter[money]
                id_type = parameter[id_type]
                id_type = id_type
                b = time.clock()
                logger.info("requests时间{b}".format(b=b))

                pub_ser =PeopleinfoModelSerializer(data=request.data)
                c = time.clock()
                logger.info("获取客户的时间{c}".format(c=c))
                # logger.info(pub_ser)
                # #print('pub_ser',pub_ser)
                if pub_ser.is_valid():
                    ##print(pub_ser.validated_data)
                    pub_ser.save()
                    #return Response(pub_ser.data)
                d = time.clock()
                logger.info("保存客户的时间{d}".format(d=d))


                ### 人行的征信数据
                # People_renhang = People(names,ids,phone,id_type)
                # dict_credit_group, dict_credit_child = People_renhang.renhanghongxian()
                e = time.clock()
                logger.info("获取人行的数据{e}".format(e=e))
                ### 逻辑回归的模型特征
                bairong = Bairong(names,ids,phone)

                bl_json,xgb_score = bairong.moxing_tz()
                #print('xgb_scorexgb_scorexgb_scorexgb_score',xgb_score)
                f = time.clock()
                logger.info("获取三方数据{f}".format(f=f))
                if 'tongdun' in bl_json.keys() or 'bairong' in bl_json.keys():
                    ret['full_name'] = names
                    ret['id_no'] = ids
                    # ret['dict_credit_group'] = dict_credit_group
                    ret['dict_credit_group'] = 0
                    ret['bl_json'] = bl_json

                    ret['cl_td'] = -99
                    ret['cl_br'] = -99

                    ret['df1_dict'] = -99
                    ret['score'] = -99
                    jsonss_ser = jsonssModelSerializer(data=ret)
                    ##print(jsonss_ser.is_valid())

                    if jsonss_ser.is_valid(raise_exception=False):
                        jsonss_ser.save()
                        # #print('ccccc')
                    else:
                        # #print(form_obj.clean_data)
                        ##print('aaaaaaaaaaaaaaaaaaaaaa',jsonss_ser.errors)
                        return jsonss_ser.errors
                    ret = {"code": 6000}
                    names = parameter[full_name]
                    ids = parameter[id_no]
                    cntent = names + str(ids) + '6000'
                    mail = SendMail(content=cntent)
                    mail.send_mail()
                    return HttpResponse(json.dumps(ret, ensure_ascii=False),content_type="application/json,charset=utf-8")
                else:
                    ret['full_name'] = names
                    ret['id_no'] = ids
                    #ret['dict_credit_group'] = dict_credit_group
                    ret['dict_credit_group'] = 0
                    ret['bl_json'] = bl_json
                    ### 策略的数据
                    tongdun_cl = sanfang(names,ids,phone)
                    # dict_br = tongdun_cl.all_cl()
                    dict_strategy_group, dict_strategy_group_br= tongdun_cl.all_cl()
                    ret['cl_td'] = dict_strategy_group
                    ret['cl_br'] =  dict_strategy_group_br

                    ### 模型的数据
                    df = pd.DataFrame([bl_json])
                    df['融资金额'] = money
                    # #print(df.dtypes)
                    df['als_m12_id_nbank_orgnum'] = df['als_m12_id_nbank_orgnum'].apply(lambda x:float(x))
                    df['frg_list_level'] = df['frg_list_level'].apply(lambda x: float(x))
                    df['ir_m6_cell_x_linkman_cell_cnt'] = df['ir_m6_cell_x_linkman_cell_cnt'].apply(lambda x: float(x))
                    df1 = score.predict(df)
                    df1_dict = df1.to_dict(orient='records')
                    ret['df1_dict'] = df1_dict
                    ret['score'] = {'td_score':max(ret['cl_td'].values()),
                                    'br_score':max(ret['cl_br'].values()),
                                    'score_mx':df1_dict[0]['score'],
                                   'xgb_score':float(xgb_score)

                    }
                    g = time.clock()
                    logger.info("输出最终数据{g}".format(g=g))
                    # ret_json = json.dumps(ret)
                    # #print('ret_jsonret_jsonret_json',ret.keys())
                    # #data = JSONParser().parse(ret)
                    jsonss_ser = jsonssModelSerializer(data=ret)
                    #print(jsonss_ser.is_valid())

                    if jsonss_ser.is_valid(raise_exception=False) :
                        jsonss_ser.save()
                        h = time.clock()
                        logger.info("保存数据{h}".format(h=h))
                        ##print('ccccc')
                    else:
                    # #print(form_obj.clean_data)
                        #print('errorserrorserrorserrorserrorserrors',jsonss_ser.errors)
                        return jsonss_ser.errors
                    if ret['score']['score_mx'] > 715 and ret['dict_credit_group'] <100  \
                        and ret['score']['td_score'] < 80 and ret['score']['br_score'] < 80:
                        status = 1000
                    elif ret['score']['score_mx'] < 405 or ret['dict_credit_group'] == 100  \
                        or (ret['score']['td_score'] > 80 and ret['score']['br_score']) > 80:
                        status = 3000
                    else:
                        status = 2000
                    statuss = {'codes':status}
                    l= time.clock()
                    logger.info("结束时间{l}".format(l=l))
                    delates= l-a
                    logger.info("总共用时间是{delates}".format(delates=delates))
                    return HttpResponse(json.dumps(statuss , ensure_ascii=False), content_type="application/json,charset=utf-8")
            else:
                ret = {"code": 4000}
                names = parameter[full_name]
                ids = parameter[id_no]
                cntent = names + str(ids)+'4000'
                mail = SendMail(content=cntent)
                mail.send_mail()
                return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")
        except:
            names = parameter[full_name]
            ids = parameter[id_no]
            cntent = names + str(ids) + '5000'
            mail = SendMail(content=cntent)
            mail.send_mail()
            ret = {"code": 5000}
            return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type="application/json,charset=utf-8")




class yunwei(APIView):
    def get(self, request):
        a = '40000'
        return HttpResponse(a)