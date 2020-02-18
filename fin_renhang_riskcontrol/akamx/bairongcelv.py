
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

"""
处理策略的模块
"""
import json
from bs4 import BeautifulSoup
import requests
from akamx.lujing import lujings
# from akamx.jisuan import Cl_score
from akamx.cljiusan import Cl_score
cl_score = Cl_score()

lujins = lujings()
www = lujins.shenfen()



import logging
logger = logging.getLogger('django')


from Gonghangguize.settings import develop as dd

from Gonghangguize.settings import product as pp
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


import datetime
today = datetime.datetime.today()
a = today.strftime("%Y-%m-%d %H:%M:%S")
b = a.replace('-','')
c =b.replace(':','')
d = c.replace(' ','')

class sanfang:


    def __init__(self, full_name, id_no, cellphone):
        self.full_name = full_name
        self.id_no = id_no
        self.cellphone = cellphone
    def suiji(self):
        ids = self.id_no[0:16]

        hsa_business_no = d+ids
        return hsa_business_no


    def bairong(self):

        hsa_business_no = self.suiji()
        results_dicts = {}
        list_all = [ 'credit100.credit100_person_apply_loan' ,'credit100.credit100_person_special_list'
                    ,'credit100.credit100_person_execution',
                     'credit100.credit100_person_fraud_relation' ,'credit100.credit100_person_info_relation']
        for datas in list_all:
            # print('datas',datas)
            data = {
                "hsa_method":datas,
                "hsa_version" :"v1.0.0",
                "full_name":self.full_name,
                "id_no":self.id_no,
                "cellphone":self.cellphone,
                "hsa_account_code": hsa_account_code,
                "hsa_account_key": hsa_account_key,
                "hsa_business_no": hsa_business_no
            }

            body = requests.post(url,data =data)

            soup = BeautifulSoup(body.text,"lxml")

            dict_all = json.loads(soup.get_text())
            # print('dict_all',dict_all)
            if 'result_list' in dict_all.keys():
                results_a = json.loads(dict_all['result_list'])

                results_dicts.update(results_a)
        # print(results_dicts)
        return results_dicts
    def bai_celo(self,results_dicts):
        BR_strategy_child = ['ir_m6_cell_x_tel_home_cnt', 'ir_m6_cell_x_biz_addr_cnt', 'ir_m6_cell_x_home_addr_cnt',
                         'ir_m6_cell_x_id_cnt', 'ir_m6_cell_x_mail_cnt', \
                         'als_m12_cell_max_monnum', 'als_m12_id_max_monnum', 'als_m1_cell_caon_allnum',
                         'als_m1_id_caon_allnum', 'als_m1_cell_nbank_week_allnum', \
                         'als_m12_cell_nbank_week_allnum', 'als_m1_id_nbank_week_allnum',
                         'als_m12_id_nbank_week_allnum', 'ex_bad1_name', 'ex_bad1_performance', \
                         'ex_bad2_name', 'ex_bad2_performance', 'ex_bad3_name', 'ex_bad3_performance',
                         'ex_bad4_name', 'ex_bad4_performance', 'ex_bad5_name', \
                         'ex_bad5_performance', 'ex_bad6_name', 'ex_bad6_performance', 'ex_bad7_name',
                         'ex_bad7_performance', 'ex_bad8_name', 'ex_bad8_performance', \
                         'ex_bad9_name', 'ex_bad9_performance', 'ex_bad_name_performance', 'als_m6_nsloan_count',
                         'als_m6_cons_count', 'als_m6_autofin_count', \
                         'als_m6_sloan_count', 'als_m6_finlea_count', 'als_m6_else_count', 'als_m12_nsloan_count',
                         'als_m12_cons_count', 'als_m12_autofin_count', \
                         'als_m12_sloan_count', 'als_m12_finlea_count', 'als_m12_else_count',
                         'alm_d7_cell_nbank_else_allnum', 'alm_d15_cell_nbank_allnum', \
                         'als_m1_cell_nbank_else_allnum', 'alm_d7_id_nbank_else_allnum', 'alm_d15_id_nbank_allnum',
                         'als_m1_id_nbank_else_allnum', 'als_m1_cell_pdl_allnum', \
                         'als_m3_cell_pdl_allnum', 'als_m1_id_pdl_allnum', 'als_m3_id_pdl_allnum',
                         'als_m6_rel_count', 'als_m6_pdl_count', 'als_m6_caon_count', \
                         'als_m6_caoff_count', 'als_m6_coon_count', 'als_m6_cooff_count', 'als_m6_af_count',
                         'als_m6_oth_count', 'als_m12_rel_count', 'als_m12_pdl_count', \
                         'als_m12_caon_count', 'als_m12_caoff_count', 'als_m12_coon_count', 'als_m12_cooff_count',
                         'als_m12_af_count', 'als_m12_oth_count', 'als_m1_rel_count', \
                         'als_m1_pdl_count', 'als_m1_caon_count', 'als_m1_caoff_count', 'als_m1_coon_count',
                         'als_m1_cooff_count', 'als_m1_af_count', 'als_m1_oth_count', \
                         'als_m3_rel_count', 'als_m3_pdl_count', 'als_m3_caon_count', 'als_m3_caoff_count',
                         'als_m3_coon_count', 'als_m3_cooff_count', 'als_m3_af_count', \
                         'als_m3_oth_count', 'als_m12_cell_nbank_allnum', 'als_m12_cell_nbank_else_allnum',
                         'als_m12_id_nbank_allnum', 'als_m12_id_nbank_else_allnum', \
                         'als_m12_cell_oth_allnum', 'als_m12_id_oth_allnum', 'als_m12_cell_pdl_allnum',
                         'als_m12_id_pdl_allnum', 'als_m1_nsloan_count', 'als_m1_cons_count', \
                         'als_m1_autofin_count', 'als_m1_sloan_count', 'als_m1_finlea_count', 'als_m1_else_count',
                         'als_m6_cell_caon_allnum', 'als_m6_id_caon_allnum', \
                         'als_m12_cell_caon_allnum', 'als_m12_id_caon_allnum', 'als_m12_cell_nbank_night_orgnum',
                         'als_m12_id_nbank_night_orgnum', 'sl_id_bad_info', \
                         'sl_id_bad_info_time', 'ex_execut1_name', 'ex_execut1_statute', 'ex_execut2_name',
                         'ex_execut2_statute', 'ex_execut3_name', 'ex_execut3_statute', \
                         'ex_execut4_name', 'ex_execut4_statute', 'ex_execut5_name', 'ex_execut5_statute',
                         'ex_execut6_name', 'ex_execut6_statute', 'ex_execut7_name', \
                         'ex_execut7_statute', 'ex_execut8_name', 'ex_execut8_statute', 'ex_execut9_name',
                         'ex_execut9_statute', 'ex_execut_statute', 'ir_m6_id_x_biz_addr_cnt', \
                         'ir_m6_id_x_home_addr_cnt', 'ir_m6_id_x_tel_home_cnt', 'ir_m6_id_x_cell_cnt',
                         'ir_m6_id_x_mail_cnt', 'ir_m12_id_x_home_addr_cnt', 'ir_m12_id_x_tel_home_cnt', \
                         'ir_m12_id_x_cell_cnt', 'ir_m12_id_x_mail_cnt', 'ir_m3_id_x_tel_home_cnt',
                         'ir_id_x_cell_cnt', 'ir_id_x_mail_cnt', 'als_m12_organization_typeall', \
                         'als_d15_cell_cooff_allnum', 'als_d15_id_cooff_allnum', 'als_m12_id_cooff_orgnum',
                         'als_m12_cell_cooff_orgnum', 'als_m2_autofin_count', \
                         'ald_cell_nbank_allnum', 'ald_id_nbank_allnum', 'sl_id_bank_bad', 'sl_id_bank_bad_time',
                         'sl_cell_bank_bad', 'sl_cell_bank_bad_time', 'sl_id_bank_fraud', \
                         'sl_id_bank_fraud_time', 'sl_cell_bank_fraud', 'sl_cell_bank_fraud_time',
                         'sl_id_bank_overdue', 'sl_id_bank_overdue_time', 'sl_cell_bank_overdue', \
                         'sl_cell_bank_overdue_time', 'sl_id_court_executed', 'sl_id_court_executed_time' \
                         ]
        # print('results_dicts.keys()',results_dicts.keys())

        td_in = [x for x in BR_strategy_child if x  in results_dicts.keys()]
        # td_notin = [x for x in BR_strategy_child if x  in results_dicts.keys()]
        # print('tdddddddddddddddd',td_in)
        dict_br = {}
        if results_dicts['flag_applyloanstr'] == '1':
            for td in BR_strategy_child:
                if td in td_in:
                    if is_Chinese(results_dicts[td]):
                        dict_br[td] = results_dicts[td]
                    else:
                        dict_br[td] = float(results_dicts[td])
                else:
                    dict_br[td] = -111
        else:
            for td in BR_strategy_child:
                dict_br[td] = -222
        return dict_br
    def tongduncelv(self):
        hsa_business_no = self.suiji()
        data = {
            "hsa_method": "tongdun.tongdun_loan_bodyguard",
            "hsa_version": "v1.0.0",
            "full_name":self.full_name,
            "id_no":self.id_no,
            "cellphone":self.cellphone,
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
        dict_a = {}
        # dict_moxing = {}
        td_list = []
        dict_moxing = {"success":None}
        if hsa_origin_message['success'] is True:
            dict_moxing = {"success": True}
            for ii in indicatrix:
                # print("iiii",ii)
                lista = ii.keys()
                dict_a = ii
                dict_moxing.update(dict_a)
                # print(lista)
                td_list += lista

        else:
            dict_moxing = {"success": False}
                # print('ddd',dd)i_get_node_rank_value_Loan_all_all
        # print('tttttttttttttddddddddddd',dict_moxing)
        return dict_moxing
    def td_cl(self,dict_moxing):
        TD_strategy_child = ['i_freq_policy_Review_all_all_60day', 'i_max_cnt_partner_daily_Loan_P2pweb_90day',
                         'i_max_cnt_partner_daily_Loan_Imbank_60day', \
                         'i_freq_policy_Reject_all_all_30day',
                         'i_max_cnt_partner_daily_Loan_Unconsumerfinance_60day',
                         'm_max_cnt_partner_daily_Loan_Imbank_60day', \
                         'i_freq_policy_Reject_all_all_90day', 'm_freq_policy_Review_all_all_30day',
                         'i_cnt_partner_last2ndmth_Loan_Bank_365day', \
                         'm_max_cnt_partner_daily_Loan_P2pweb_60day', 'm_max_cnt_partner_daily_Loan_all_90day',
                         'm_max_cnt_partner_daily_Loan_Offloan_90day', \
                         'm_max_cnt_partner_daily_Loan_P2pweb_90day', 'i_max_cnt_partner_daily_Loan_finance_60day',
                         'i_max_cnt_partner_daily_Loan_Imbank_90day', \
                         'm_max_cnt_partner_daily_Loan_finance_365day', 'i_freq_policy_Review_all_all_90day',
                         'i_pctl_cnt_ic_partner_Loan_Imbank_60day', \
                         'm_max_cnt_partner_daily_Loan_finance_60day', 'i_max_cnt_partner_daily_Loan_Imbank_30day',
                         'i_max_cnt_partner_daily_Loan_Imbank_365day', \
                         'i_cnt_partner_last6thmth_Loan_all_365day', 'm_freq_policy_Review_all_all_60day',
                         'i_max_cnt_partner_daily_Loan_finance_90day', \
                         'm_max_cnt_partner_daily_Loan_con_365day', 'i_max_cnt_partner_daily_Loan_finance_180day',
                         'm_max_cnt_partner_daily_Loan_all_60day', \
                         'm_max_cnt_partner_daily_Loan_all_30day', 'i_max_cnt_partner_daily_Loan_Offloan_90day',
                         'i_cnt_partner_last3rdmth_Loan_Imbank_365day', \
                         'i_pctl_cnt_ic_partner_Loan_Imbank_365day', 'm_max_cnt_partner_daily_Loan_Offloan_365day',
                         'm_freq_policy_Reject_all_all_30day', \
                         'm_pctl_cnt_ic_partner_Loan_Imbank_90day', 'i_freq_policy_Reject_all_all_180day',
                         'm_cnt_partner_last1stmth_Loan_Imbank_365day', \
                         'm_max_cnt_partner_daily_Loan_con_90day', 'i_max_cnt_partner_daily_Loan_P2pweb_60day',
                         'i_cnt_partner_last4thmth_Loan_IFinanceWeb_365day', \
                         'i_pctl_cnt_ic_partner_Loan_Imbank_180day', 'i_pctl_cnt_ic_partner_Loan_Bank_365day',
                         'm_cnt_partner_last1stmth_Loan_all_365day', \
                         'm_pctl_cnt_ic_partner_Loan_Imbank_30day', 'i_cnt_partner_last2ndmth_Loan_Imbank_365day',
                         'i_max_cnt_partner_daily_Loan_P2pweb_180day', \
                         'i_max_cnt_partner_daily_Loan_Unconsumerfinance_30day',
                         'i_freq_policy_Reject_all_all_365day', 'm_max_cnt_partner_daily_Loan_con_180day', \
                         'i_max_cnt_partner_daily_Loan_con_90day',
                         'i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day', 'i_freq_policy_Reject_all_all_60day', \
                         'i_freq_policy_Review_all_all_30day', 'm_get_node_rank_value_Loan_all_all',
                         'i_max_cnt_partner_daily_Loan_Imbank_180day', \
                         'i_cnt_partner_last1stmth_Loan_Imbank_365day', 'm_cnt_partner_last3rdmth_Loan_all_365day',
                         'i_pctl_cnt_ic_partner_Loan_Imbank_90day', \
                         'i_max_cnt_partner_daily_Loan_P2pweb_30day', 'i_cnt_node_dist1_device_Loan_all_all',
                         'i_max_cnt_partner_daily_Loan_P2pweb_365day', \
                         'm_cnt_partner_last2ndmth_Loan_all_365day', 'm_cnt_node_partner_Loan_all_all',
                         'i_cnt_partner_last2ndmth_Loan_IFinanceWeb_365day', \
                         'm_max_cnt_partner_daily_Loan_Imbank_365day', 'm_cnt_partner_last5thmth_Loan_all_365day',
                         'i_cnt_node_dist1_cmobile_Loan_all_all', \
                         'i_pctl_cnt_ic_partner_Loan_Bank_60day', 'i_pctl_cnt_ic_partner_Loan_Imbank_30day',
                         'm_ratio_cnt_node_dist1_device_Loan_all_all', \
                         'm_ratio_cnt_node_dist2_id_Loan_all_all',
                         'm_max_cnt_partner_daily_Loan_Unconsumerfinance_90day',
                         'i_cnt_partner_last3rdmth_Loan_all_365day', \
                         'i_freq_policy_Accept_all_all_90day',
                         'i_max_cnt_partner_daily_Loan_Unconsumerfinance_365day',
                         'm_max_cnt_partner_daily_Loan_con_30day', \
                         'i_max_cnt_partner_daily_Loan_con_180day', 'm_freq_policy_Accept_all_all_180day',
                         'i_freq_policy_Accept_all_all_30day', \
                         'm_cnt_partner_last3rdmth_Loan_Imbank_365day', 'i_get_node_rank_value_Loan_all_all',
                         'm_cnt_node_dist2_Loan_all_all', \
                         'i_freq_policy_Review_all_all_365day', 'i_cnt_partner_last6thmth_Loan_Imbank_365day',
                         'i_pctl_cnt_ic_partner_Loan_Bank_90day', \
                         'm_ratio_cnt_grp_reject_review_Loan_all_all', 'm_cnt_partner_last1stmth_Loan_Bank_365day',
                         'm_cnt_partner_last4thmth_Loan_Imbank_365day', \
                         'i_max_cnt_partner_daily_Loan_Inconsumerfinance_90day',
                         'i_max_cnt_partner_daily_Loan_Consumerfinance_90day',
                         'm_ratio_cnt_grp_device_Loan_all_all', \
                         'i_max_cnt_partner_daily_Loan_con_30day', 'i_cnt_partner_last4thmth_Loan_Bank_365day',
                         'm_cnt_partner_last2ndmth_Loan_Imbank_365day', \
                         'm_freq_policy_Accept_all_all_60day', 'i_pctl_cnt_ic_partner_Loan_Bank_180day',
                         'm_freq_policy_Reject_all_all_60day', 'i_cnt_node_dist1_Loan_all_all', \
                         'i_cnt_partner_last3rdmth_Loan_Bank_365day', 'm_ratio_cnt_node_reject_Loan_all_all',
                         'i_max_cnt_partner_daily_Loan_Offloan_180day', \
                         'i_max_cnt_partner_daily_Loan_con_365day', 'i_ratio_cnt_node_dist1_device_Loan_all_all',
                         'm_max_cnt_partner_daily_Loan_Offloan_180day', \
                         'm_ratio_cnt_node_dist2_device_Loan_all_all', 'm_freq_policy_Accept_all_all_30day',
                         'i_freq_policy_Accept_all_all_365day', \
                         'm_max_cnt_partner_daily_Loan_P2pweb_365day',
                         'i_max_cnt_partner_daily_Loan_Consumerfinance_180day',
                         'm_ratio_cnt_node_reject_review_Loan_all_all', \
                         'i_cnt_partner_last1stmth_Loan_Bank_365day', 'i_cnt_partner_last5thmth_Loan_Bank_365day',
                         'm_cnt_partner_last2ndmth_Loan_Bank_365day', \
                         'm_pctl_cnt_ic_partner_Loan_Bank_365day', 'i_cnt_partner_last6thmth_Loan_Bank_365day',
                         'm_cnt_node_dist1_Loan_all_all', \
                         'i_cnt_partner_last5thmth_Loan_IFinanceWeb_365day', 'i_freq_policy_Review_all_all_180day',
                         'm_cnt_node_reject_Loan_all_all', \
                         'i_cnt_partner_last3rdmth_Loan_Insurance_365day',
                         'm_max_cnt_partner_daily_Loan_Consumerfinance_365day', \
                         'i_max_cnt_partner_daily_Loan_Inconsumerfinance_365day',
                         'm_cnt_partner_last6thmth_Loan_Bank_365day', 'm_freq_policy_Review_all_all_180day', \
                         'm_ratio_cnt_grp_mobile_Loan_all_all', 'm_pctl_cnt_ic_partner_Loan_Bank_180day',
                         'm_pctl_cnt_ic_partner_Loan_Imbank_365day', \
                         'm_max_cnt_partner_daily_Loan_Unconsumerfinance_365day',
                         'm_max_cnt_partner_daily_Loan_P2pweb_30day', 'm_freq_policy_Accept_all_all_90day', \
                         'm_cnt_node_dist2_device_Loan_all_all', 'i_freq_policy_Accept_all_all_60day',
                         'm_max_cnt_partner_daily_Loan_Imbank_30day', \
                         'i_cnt_node_dist1_card_Loan_all_all', 'm_pctl_cnt_ic_partner_Loan_Imbank_60day',
                         'm_max_cnt_partner_daily_Loan_Unconsumerfinance_60day', \
                         'i_max_cnt_partner_daily_Loan_Consumerfinance_365day',
                         'i_cnt_partner_last4thmth_Loan_all_365day', 'm_freq_policy_Review_all_all_365day', \
                         'i_max_cnt_partner_daily_Loan_all_30day', 'i_cnt_node_partner_Loan_all_all',
                         'm_freq_policy_Reject_all_all_180day', \
                         'i_max_cnt_partner_daily_Loan_con_60day',
                         'm_max_cnt_partner_daily_Loan_Consumerfinance_180day', 'i_is_core_node_Loan_all_all', \
                         'i_ratio_cnt_node_reject_Loan_all_all', 'm_ratio_cnt_node_review_Loan_all_all',
                         'i_cnt_node_dist1_mobile_Loan_all_all', \
                         'i_cnt_node_dist2_id_Loan_all_all', 'm_max_cnt_partner_daily_Loan_P2pweb_180day',
                         'm_cnt_partner_last5thmth_Loan_Bank_365day' \
                         ]
        td_dict = {}
        if dict_moxing['success']:
            td_dict = {'success': "返回成功"}
            for uu in TD_strategy_child:
                name_v = dict_moxing[uu]
                if name_v is None:
                    td_dict[uu] = -333
                else:
                    td_dict[uu] = float(name_v)
        else:
            td_dict = {'success': "返回失败"}
            for uu in TD_strategy_child:
                td_dict[uu] = -555

        return td_dict
    def all_cl(self):
        results_dicts = self.bairong()
        dict_br = self.bai_celo(results_dicts)
        # score_br= max(dict_br.values())
        td_dict = self.tongduncelv()
        td_cl = self.td_cl(td_dict)
        # score_td = td_cl.values()
        # print('zzzzzzzzzzzzzzzzzzzzzzzzz',score_td)
        dict_br.update(td_cl)
        allcl = dict_br

        dict_strategy_group, dict_strategy_group_br =cl_score.cl_score(dict_br)
        return dict_strategy_group, dict_strategy_group_br
        # return dict_br