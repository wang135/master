from pickle import load
import json
from bs4 import BeautifulSoup
import requests
import datetime

from akamx.lujing import lujings

from akamx.xgboost import xgboost
import time
import pandas as pd
import logging
logger = logging.getLogger('django')
from akamx.sanfangshuju import Datas



class Bairong:
    def __init__(self,full_name,id_no,cellphone,id_type):
        self.full_name =full_name
        self.id_no = id_no
        self.cellphone = cellphone
        self.id_type = id_type

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
    def bar_moing(self,results_dicts):
        www = lujings().shenfen()
        # print('wwwwwwwwwwwwwwwwwwwwwwwwwww',www)
        # print(results_dicts)
        # www['号段'] = www['号段'].astype('str')

        cell_province = lujings().cell_province()
        cell_province['cell_province'] = cell_province['cell_province'].str.strip()

        cell_city = lujings().cell_city()[['cell_city','ids']]
        cell_city['cell_city'] = cell_city['cell_city'].str.strip()
        #results_dicts = self.requestss()
        if results_dicts != 4000:
            try:
                ###print('results_dictsresults_dictsresults_dictsresults_dicts',results_dicts)
                dict_sex = self.sex_gender()
                ### 获取百融数据的result_list

                ###取百融模型
                bl_json = {}
                list_binaliang = ['als_m12_id_nbank_orgnum', 'frg_list_level', 'ir_m6_cell_x_linkman_cell_cnt',
                                  'flag_specialList_c']
                if results_dicts['flag_applyloanstr'] == '1':
                    for ii in list_binaliang:
                        if ii in results_dicts.keys():
                            bl_json[ii] = results_dicts[ii]
                        else:
                            bl_json[ii] = -1
                else:
                    bl_json = {'als_m12_id_nbank_orgnum': -99, 'frg_list_level': -99,
                               'ir_m6_cell_x_linkman_cell_cnt': -99, 'flag_specialList_c': -99}
                # ##print(bl_json)

                # model_path = r"C:\Users\Administrator\shenfen.pickle"

                www['号段'] = www['号段'].apply(lambda x: str(x))
                ###print('www',www)
                phon_a = self.cellphone[0:7]
                ss = www[www['号段'] == phon_a]

                ### LR的模型
                ss_dict = ss.to_dict(orient='records')[0]
                bl_json.update(ss_dict)
                bl_json.update(dict_sex)
                ##print('ccccccccccccccccccccccccc')
                ##print(cell_province)
                ##print('cell_city',cell_city)
                xgb = xgboost(results_dicts,ss,dict_sex)
                datas = xgb.join()
                id_city = xgb.id_shenfen(self.id_no)
                datas['id_city'] = id_city
                ##print('dadadadaaaa',datas['id_city'])
                xgb_score = xgb.datas(datas)

                return bl_json,xgb_score
            except:
                bl_json={'bairong':4000}
                xgb_score = [0]
                return bl_json,xgb_score
        else:
            bl_json = {'bairong': 4000}
            xgb_score = [0]
            return bl_json,xgb_score

    def tongdun_jisuan(self,hsa_origin_message):
        if hsa_origin_message !=4000:
            indicatrix = hsa_origin_message['result_desc']['PERSONASPRELOAN']['indicatrix']
            dict_moxing = {}
            if hsa_origin_message['success'] is True:
                list_moxing = ["i_max_cnt_partner_daily_Loan_finance_365day", "i_get_node_rank_value_Loan_all_all"]

                for ii in indicatrix:
                    # ##print("iiii",ii)
                    if list_moxing[0] in ii.keys():
                        i_max_cnt_partner_daily_Loan_finance_365day = ii[list_moxing[0]]

                        ##print('ccc', i_max_cnt_partner_daily_Loan_finance_365day)

                        if i_max_cnt_partner_daily_Loan_finance_365day is None:
                            dict_moxing['i_max_cnt_partner_daily_Loan_finance_365day'] = -1111

                        else:
                            dict_moxing[
                                'i_max_cnt_partner_daily_Loan_finance_365day'] = i_max_cnt_partner_daily_Loan_finance_365day
                    elif list_moxing[1] in ii.keys():
                        i_get_node_rank_value_Loan_all_all = ii[list_moxing[1]]
                        ##print('ddd', i_get_node_rank_value_Loan_all_all)
                        if i_get_node_rank_value_Loan_all_all is None:
                            dict_moxing['i_get_node_rank_value_Loan_all_all'] = -1111
                        else:
                            dict_moxing['i_get_node_rank_value_Loan_all_all'] = i_get_node_rank_value_Loan_all_all
                            # ##print('ddd',dd)i_get_node_rank_value_Loan_all_all

            else:
                dict_moxing = {'i_max_cnt_partner_daily_Loan_finance_365day': -999,
                               'i_get_node_rank_value_Loan_all_all': -999}
            return dict_moxing
        else:
            #### 同盾的数据获取失败
            codes = 5000
            dict_moxing = {'tongdun':codes}
            return dict_moxing
    def moxing_tz(self):
        aa = time.clock()

        results_br = Datas(self.full_name,self.id_no,self.cellphone,self.id_type).requestss()
        bb = time.clock()
        cc = bb-aa
        logger.info("百融数据结束{cc}".format(cc=cc))
        # print('1111111111111111111',results_br)

        ##print('kaishikaishisssssssssssssssssssssssssss')
        bl_json,xgb_score = self.bar_moing(results_br)
        dd = time.clock()
        da = dd-bb
        logger.info("XGBOOST{da}".format(da=da))
        results_td = Datas(self.full_name,self.id_no,self.cellphone,self.id_type).tongdun_requests()
        # print('1111111111111111111', results_br)
        #results_td = self.tongdun_requests()
        td_jisuan = self.tongdun_jisuan(results_td)
        bl_json.update(td_jisuan)


        return bl_json,xgb_score[0]


