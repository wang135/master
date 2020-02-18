from pickle import load
import json
from bs4 import BeautifulSoup
import requests
import datetime

from akamx.lujing import lujings



import logging
logger = logging.getLogger('django')


from Gonghangguize.settings import develop as dd

from Gonghangguize.settings import product as pp
#import Gonghangguize.settings as settings
import os
#name = os.environ.get('TYPEIDEA_PROFILE', 'develop')
profile = os.environ.get('TYPEIDEA_PROFILE', )
name = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gonghangguize.%s' %profile)
#print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',name)
if name in ['Gonghangguize.settings.develop','Gonghangguize.settings.base']:
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



#print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',name)
if name in ['Gonghangguize.settings.develop','Gonghangguize.settings.base']:
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

##随机数据
import datetime
today = datetime.datetime.today()
a = today.strftime("%Y-%m-%d %H:%M:%S")
b = a.replace('-','')
c =b.replace(':','')
d = c.replace(' ','')

lujins = lujings()
www = lujins.shenfen()
class Bairong:
    def __init__(self,full_name,id_no,cellphone):
        self.full_name =full_name
        self.id_no = id_no
        self.cellphone = cellphone
    def suiji(self):
        ids = self.id_no[0:16]

        hsa_business_no = d+ids
        return hsa_business_no
    def requestss(self):

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
            #print('soupsoupsoupsoup',soup)
            dict_all = json.loads(soup.get_text())

            if 'result_list' in dict_all.keys():
                results_a = json.loads(dict_all['result_list'])
                # results_b[datas] = results_a
                # print(results_b)
                results_dicts.update(results_a)
        return results_dicts

    def sex_gender(self):
        dict_sex = {}
        now = datetime.datetime.today()
        tt = now.strftime("%Y")
        birth = self.id_no[6:10]

        apply_age = int(tt) - int(birth)
        dict_sex['apply_age'] = apply_age

        sex = int(self.id_no[-2])
        if (sex % 2) == 0:
            dict_sex['gender'] = 0
        else:
            dict_sex['gender'] = 1
        return dict_sex
    def bar_moing(self,www):
        results_dicts = self.requestss()
        try:
            #print('results_dictsresults_dictsresults_dictsresults_dicts',results_dicts)
            dict_sex = self.sex_gender()
            ### 获取百融数据的result_list

            ###取百融模型
            bl_json = {}
            list_binaliang = ['als_m12_id_nbank_orgnum', 'frg_list_level', 'ir_m6_cell_x_linkman_cell_cnt',
                              'flag_specialList_c']
            if results_dicts['flag_applyloanstr'] == '1':
                for ii in list_binaliang:
                    # try:
                    if ii in results_dicts.keys():
                        bl_json[ii] = results_dicts[ii]
                    else:
                        bl_json[ii] = -1
            else:
                bl_json = {'als_m12_id_nbank_orgnum': -99, 'frg_list_level': -99,
                           'ir_m6_cell_x_linkman_cell_cnt': -99, 'flag_specialList_c': -99}
            # print(bl_json)

            # model_path = r"C:\Users\Administrator\shenfen.pickle"

            www['号段'] = www['号段'].apply(lambda x: str(x))
            #print('www',www)
            phon_a = self.cellphone[0:7]
            ss = www[www['号段'] == phon_a]
            #print('ss', ss)
            ss_dict = ss.to_dict(orient='records')[0]
            bl_json.update(ss_dict)
            bl_json.update(dict_sex)
            return bl_json
        except:
            bl_json={'bairong':4000}
            return bl_json

    ### 计算
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
            indicatrix = hsa_origin_message['result_desc']['PERSONASPRELOAN']['indicatrix']
            dict_moxing = {}
            if hsa_origin_message['success'] is True:
                list_moxing = ["i_max_cnt_partner_daily_Loan_finance_365day", "i_get_node_rank_value_Loan_all_all"]

                for ii in indicatrix:
                    # print("iiii",ii)
                    if list_moxing[0] in ii.keys():
                        i_max_cnt_partner_daily_Loan_finance_365day = ii[list_moxing[0]]

                        print('ccc', i_max_cnt_partner_daily_Loan_finance_365day)

                        if i_max_cnt_partner_daily_Loan_finance_365day is None:
                            dict_moxing['i_max_cnt_partner_daily_Loan_finance_365day'] = -1111

                        else:
                            dict_moxing[
                                'i_max_cnt_partner_daily_Loan_finance_365day'] = i_max_cnt_partner_daily_Loan_finance_365day
                    elif list_moxing[1] in ii.keys():
                        i_get_node_rank_value_Loan_all_all = ii[list_moxing[1]]
                        print('ddd', i_get_node_rank_value_Loan_all_all)
                        if i_get_node_rank_value_Loan_all_all is None:
                            dict_moxing['i_get_node_rank_value_Loan_all_all'] = -1111
                        else:
                            dict_moxing['i_get_node_rank_value_Loan_all_all'] = i_get_node_rank_value_Loan_all_all
                            # print('ddd',dd)i_get_node_rank_value_Loan_all_all

            else:
                dict_moxing = {'i_max_cnt_partner_daily_Loan_finance_365day': -999,
                               'i_get_node_rank_value_Loan_all_all': -999}
            return dict_moxing
        except:
            #### 同盾的数据获取失败
            codes = 5000
            dict_moxing = {'tongdun':codes}
            return dict_moxing
    def moxing_tz(self):
        bl_json = self.bar_moing(www=www)
        td_json = self.tongdun_requests()
        bl_json.update(td_json)

        return bl_json