import numpy as np

from ghrule.forms import RuleSerializer
from ghrule.models import Rule
import time
import json
import requests
import datetime
from bs4 import BeautifulSoup


from Gonghangguize.settingss import develop as dd

from Gonghangguize.settingss import product as pp
#import Gonghangguize.settingss as settingss
import socket

myname = socket.getfqdn(socket.gethostname(  ))
myaddr = socket.gethostbyname(myname)


import logging
logger = logging.getLogger('django')

hsa_account_code = ''
hsa_account_key = ''
url = ''
if myaddr in ['172.16.1.116', '172.16.1.105','10.254.0.245']:
    hsa_account_code = dd.hsa_account_code_cs
    hsa_account_key = dd.hsa_account_key_cs
    hsa_method = dd.hsa_method
    hsa_version = dd.hsa_version
    url = dd.url_cs
elif myaddr =='10.6.105.30':
    hsa_account_code = dd.hsa_account_code_cs
    hsa_account_key = dd.hsa_account_key_cs
    hsa_method = dd.hsa_method
    hsa_version = dd.hsa_version
    url = dd.url_cs
else:
    hsa_account_code = pp.hsa_account_code_zs
    hsa_account_key = pp.hsa_account_key_zs
    hsa_method = pp.hsa_method
    hsa_version = pp.hsa_version
    url = pp.url_zs

#import Gonghangguize.settingss as settingss
import os
#name = os.environ.get('TYPEIDEA_PROFILE', 'develop')
# profile = os.environ.get('TYPEIDEA_PROFILE', )
# name = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gonghangguize.%s' %profile)
# #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',name)
# if profile in ['develop','base']:
# hsa_account_code = dd.hsa_account_code_cs
# hsa_account_key = dd.hsa_account_key_cs
# hsa_method = dd.hsa_method
# hsa_version = dd.hsa_version
# url = dd.url_cs
# else:
#     hsa_account_code = pp.hsa_account_code_zs
#     hsa_account_key = pp.hsa_account_key_zs
#     hsa_method = pp.hsa_method
#     hsa_version = pp.hsa_version
#     url = pp.url_zs

# from Gonghangguize.settingss import base as aa
#
# from Gonghangguize.settingss import develop as aa
#
# from Gonghangguize.settingss import product as aa
#import Gonghangguize.settingss as settingss


#BASE_DIR = settingss.BASE_DIR
#print('BASE_DIRBASE_DIRBASE_DIR',BASE_DIR)

import logging
logger = logging.getLogger('django')






#print('wwwwwwwwwwwww',hsa_account_code,hsa_account_key,url)

##随机数据
import datetime
today = datetime.datetime.today()
a = today.strftime("%Y-%m-%d %H:%M:%S")
b = a.replace('-','')
c =b.replace(':','')
d = c.replace(' ','')



class People:
    def __init__(self, full_name, id_no,id_type):
        self.full_name = full_name
        self.id_no = id_no
        self.id_type = id_type
    def suiji(self):
        ids = self.id_no[0:16]

        hsa_business_no = d+ids
        return hsa_business_no
    def datas(self):


        hsa_business_no = self.suiji()
        data = {
            "hsa_method": hsa_method,
            "hsa_version": hsa_version,
            "full_name": self.full_name,
            "id_no": self.id_no,
            "id_type" : self.id_type,

            "hsa_account_code": hsa_account_code,
            "hsa_account_key": hsa_account_key,
            "hsa_business_no": hsa_business_no
        }
        dict_all = ''
        n = 0
        while n <5:
            try:

                body = requests.post(url,timeout = 5, data=data)
                soup = BeautifulSoup(body.text, "lxml")

                dict_all = json.loads(soup.get_text())
                #print('sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss', dict_all)


            except:
                n+=1
            # logger.info("获取人行接口失败")

            return dict_all

        #print('dict_alldict_all',dict_all)
        # return dict_all
    ### 连三累8
    ### 连三累8
    def creditCardInfo(self,ii):
        ##连三
        list_djk_max1 = [0]
        ##累计逾期
        list_djk_len1 = []
        ###状态的形态
        accountStatus_list = []
        # ii =  data[0]
        try:
            if 'creditCardInfo' in ii['credit_result_json']['reportMessage'].keys():
                creditCardInfo = ii['credit_result_json']['reportMessage']['creditCardInfo']

                for cd in creditCardInfo:
                    if 'month24RepayStatus' in cd.keys():
                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])
                        #print(month24RepayStatus4)
                        list_djk_max1.append(month24RepayStatus_maax)

                        len_djk = len([float(x) for x in month24RepayStatus4 if float(x) > 0])

                        list_djk_len1.append(len_djk)

                        accountStatus = cd['accountStatus']
                        accountStatus_list.append(accountStatus)
                        if 'accountStatus' in cd['titleInfoObject'].keys():
                            accountStatus = cd['titleInfoObject']['accountStatus']
                            accountStatus_list.append(accountStatus)
        except:

            if 'creditCardInfo' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                creditCardInfo = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['creditCardInfo']

                for cd in creditCardInfo:
                    if 'month24RepayStatus' in cd.keys():

                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        #print(month24RepayStatus4)
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])
                        list_djk_max1.append(month24RepayStatus_maax)
                        len_djk = len([float(x) for x in month24RepayStatus4 if float(x) > 0])

                        list_djk_len1.append(len_djk)

                        accountStatus = cd['accountStatus']
                        accountStatus_list.append(accountStatus)

                        if 'accountStatus' in cd['titleInfoObject'].keys():
                            accountStatus = cd['titleInfoObject']['accountStatus']
                            accountStatus_list.append(accountStatus)

        return list_djk_max1, list_djk_len1, accountStatus_list


    ###贷款状态的收集
    def loaninfo(self,ii):
        ##连三
        list_loan_san = [0]
        ##累计逾期
        list_loan_len1 = []
        ###状态的形态
        loan_accountStatus_list = []
        # ii =  data[0]
        try:
            if 'loanInfo' in ii['credit_result_json']['reportMessage'].keys():
                creditCardInfo = ii['credit_result_json']['reportMessage']['loanInfo']

                for cd in creditCardInfo:
                    if 'month24RepayStatus' in cd.keys():
                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('D', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])
                        #print(month24RepayStatus4)
                        list_loan_san.append(month24RepayStatus_maax)

                        len_djk = len([float(x) for x in month24RepayStatus4 if float(x) > 0])

                        list_loan_len1.append(len_djk)

                        accountStatus = cd['accountStatus']
                        loan_accountStatus_list.append(accountStatus)

                        if 'accountStatus' in cd['titleInfoObject'].keys():
                            accountStatus = cd['titleInfoObject']['accountStatus']
                            loan_accountStatus_list.append(accountStatus)
        except:

            if 'loanInfo' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                creditCardInfo = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['loanInfo']

                for cd in creditCardInfo:
                    if 'month24RepayStatus' in cd.keys():

                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('D', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        #print(month24RepayStatus4)
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])
                        list_loan_san.append(month24RepayStatus_maax)
                        len_djk = len([float(x) for x in month24RepayStatus4 if float(x) > 0])

                        list_loan_len1.append(len_djk)

                        accountStatus = cd['accountStatus']
                        loan_accountStatus_list.append(accountStatus)

                        if 'accountStatus' in cd['titleInfoObject'].keys():
                            accountStatus = cd['titleInfoObject']['accountStatus']
                            loan_accountStatus_list.append(accountStatus)
        return list_loan_san, list_loan_len1, loan_accountStatus_list

    ## 保证人代偿
    ## 保证人代偿
    def cumulativeCompenAmounts(self,ii):
        cumulativeCompenAmount = 0
        list_cumulativeCompenAmount = [0]
        try:
            if 'gciList' in ii['credit_result_json']['reportMessage'].keys():
                cumulativeCompenAmount = ii['credit_result_json']['reportMessage']['gciList'][0][
                    'cumulativeCompenAmount'].replace(',', '')
                cumulativeCompenAmount = float(cumulativeCompenAmount)

            else:
                cumulativeCompenAmount = 0
            list_cumulativeCompenAmount.append(cumulativeCompenAmount)
        except:

            if 'gciList' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                cumulativeCompenAmount = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['gciList'][0][
                    'cumulativeCompenAmount'].replace(',', '')
                cumulativeCompenAmount = float(cumulativeCompenAmount)
                list_cumulativeCompenAmount.append(cumulativeCompenAmount)
                #print('cumulativeCompenAmount', cumulativeCompenAmount)
            else:
                cumulativeCompenAmount = 0
            list_cumulativeCompenAmount.append(cumulativeCompenAmount)
        return list_cumulativeCompenAmount


    ### 外贷款担保信息
    def danbao(self,ii):
        status = ["关注", "次级", "可疑", "损失"]
        list_loan_danbao = []
        fiveClassify = 'wu'
        try:
            if 'lgiList' in ii['credit_result_json']['reportMessage'].keys():
                fiveClassify = ii['credit_result_json']['reportMessage']['lgiList'][0]['fiveClassify']
                print('fiveClassify', fiveClassify)
                # list_loan_danbao.append(fiveClassify)
                if fiveClassify in status:
                    fiveClassify = fiveClassify
                    list_loan_danbao.append(fiveClassify)



        except:

            if 'lgiList' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                fiveClassify = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['lgiList'][0]['fiveClassify']
                print('fiveClassify', fiveClassify)
                list_loan_danbao.append(fiveClassify)
                if fiveClassify in status:
                    fiveClassify = fiveClassify
                    list_loan_danbao.append(fiveClassify)
        return fiveClassify

    def renhanhgomngshang(self):

        ee = time.clock()
        logger.info("调取人行接口开始时间{ee}".format(ee=ee))
        ii = self.datas()
        #print('sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss', ii)
        ff = time.clock()
        logger.info("调取人行接口结束时间{ff}".format(ff=ff))
        huoqu = ff - ee
        logger.info("调取人行接口总共所用时间{huoqu}".format(huoqu=huoqu))

        #print('rrrr',ii['credit_result_json']['reportMessage'].keys())
        code = ii['hsa_status']
        #
        #print('codecode',code)
        if code ==1:
            list_djk_max1, list_djk_len1, accountStatus_list = self.creditCardInfo(ii)

            list_loan_san, list_loan_len1, loan_accountStatus_list = self.loaninfo(ii)

            list_loan_danbao = self.danbao(ii)

            list_cumulativeCompenAmount = self.cumulativeCompenAmounts(ii)

            ### 计算连三累八
            all_list_san = list_djk_max1 + list_loan_san
            all_list_san.append(0)
            list_len_all = list_djk_len1 + list_loan_len1
            list_len_all.append(0)
            #### 计算状态
            accountStatus_all = accountStatus_list + loan_accountStatus_list + list(list_loan_danbao)
            status = ["关注", "次级", "可疑", "损失"]
            list_condit = [x for x in accountStatus_all if x in status]
            ###计算代偿金额
            cumulativeCompenAmount = max(list_cumulativeCompenAmount)
            ### 字段写入数据库
            # rule = Rule()
            # rule.full_name = self.full_name
            # rule.id_no = self.id_no
            # rule.all_list_san = max(all_list_san)
            # rule.list_len_all = max(list_len_all)
            #
            # rule.cumulativeCompenAmount = cumulativeCompenAmount
            # rule.condit = len(list_condit)
            # rule.save()
            n = 0
            while n < 5:
                try:
                    rule = Rule()
                    rule = Rule()
                    rule.full_name = self.full_name
                    rule.id_no = self.id_no
                    rule.all_list_san = max(all_list_san)
                    rule.list_len_all = max(list_len_all)

                    rule.cumulativeCompenAmount = cumulativeCompenAmount
                    rule.condit = len(list_condit)
                    rule.save()
                    break
                except:
                    n += 1

            if max(all_list_san) > 3 or max(list_len_all) > 8 or cumulativeCompenAmount > 0 or len(list_condit) > 0:
                code = 1000
            else:
                code = 4000
            #print('code', code)
        ##
        else:
            code = 0000
        logger.info("错误的信息{code}".format(code= code))
        #mail.send_mail()
        gg = time.clock()

        logger.info("调取函数结束时间{gg}".format(gg=gg))
        all_time =gg-ee
        logger.info("总共所用时间{all_time}".format(all_time=all_time))
        diff_hanshu = huoqu/all_time
        logger.info("调取人行数据和总函数时间的比例{diff_hanshu}".format(diff_hanshu=diff_hanshu))
        return code