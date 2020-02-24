

from Gonghangguize.settings import develop as dd

from Gonghangguize.settings import product as pp
#import Gonghangguize.settings as settings
import os
#name = os.environ.get('TYPEIDEA_PROFILE', 'develop')

profile = os.environ.get('TYPEIDEA_PROFILE', )
name = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gonghangguize.%s' %profile)
##print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',name)
if profile in ['develop','base']:
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

import json
from bs4 import BeautifulSoup
import requests



##随机数据
import datetime


class Datas:
    def __init__(self,full_name,id_no,cellphone,id_type):
        self.full_name =full_name
        self.id_no = id_no
        self.cellphone = cellphone
        self.id_type = id_type
    def suiji(self):
        today = datetime.datetime.today()
        a = today.strftime("%Y-%m-%d %H:%M:%S")
        b = a.replace('-', '')
        c = b.replace(':', '')
        d = c.replace(' ', '')
        ids = self.id_no[0:16]

        hsa_business_no = d+ids
        return hsa_business_no
    def requestss(self):
        try:
            hsa_business_no = self.suiji()
            results_dicts = {}
            list_all = ['credit100.credit100_person_apply_loan', 'credit100.credit100_person_special_list',
                        'credit100.credit100_person_execution',
                        'credit100.credit100_person_fraud_relation'
                , 'credit100.credit100_person_info_relation']
            for datas in list_all:
                data = {
                    "hsa_method": datas,
                    "hsa_version": hsa_version,
                    "full_name": self.full_name,
                    "id_no": self.id_no,
                    "cellphone": self.cellphone,
                     "hsa_account_code": hsa_account_code,
                     "hsa_account_key": hsa_account_key,
                    "hsa_business_no": hsa_business_no
                }

                body = requests.post(url, data=data)

                soup = BeautifulSoup(body.text, "lxml")
                ##print('soupsoupsoupsoup',soup)
                dict_all = json.loads(soup.get_text())

                if 'result_list' in dict_all.keys():
                    results_a = json.loads(dict_all['result_list'])
                    # results_b[datas] = results_a
                    # print(results_a)
                    results_dicts.update(results_a)
            return results_dicts
        except:
            codess = 4000
            return codess
    def tongdun_requests(self):
        try:
            hsa_business_no = self.suiji()
            data = {
                "hsa_method": "tongdun.tongdun_loan_bodyguard",
                "hsa_version": "v1.0.0",
                "full_name": self.full_name,
                "id_no": self.id_no,
                "cellphone": self.cellphone,
                 "hsa_account_code": hsa_account_code,
                 "hsa_account_key": hsa_account_key,
                "hsa_business_no": hsa_business_no
            }

            body = requests.post(url, data=data)

            soup = BeautifulSoup(body.text, "lxml")

            dict_all = json.loads(soup.get_text())

            hsa_origin_message1 = dict_all["hsa_origin_message"]
            hsa_origin_message = json.loads(hsa_origin_message1)
            return hsa_origin_message
        except:
            codess = 4000
            return 4000

    def pboc(self):
        hsa_business_no = self.suiji()
        data = {
            "hsa_method": 'credit.credit_single_query',
            "hsa_version": "v1.0.0",
            "full_name": self.full_name,
            "id_no": self.id_no,
            "cellphone": self.cellphone,
            "id_type": self.id_type,
            "hsa_account_code": hsa_account_code,
            "hsa_account_key": hsa_account_key,
            "hsa_business_no": hsa_business_no
        }

        body = requests.post(url, data=data)
        soup = BeautifulSoup(body.text, "lxml")

        dict_all = json.loads(soup.get_text())
        return dict_all