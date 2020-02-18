

import json
from bs4 import BeautifulSoup
import requests
url = 'http://test-credit.huashenghaoche.com/hshccredit/gateway/request'
class Tongdun:
    def __init__(self,full_name,id_no,cellphone):
        self.full_name =full_name
        self.id_no = id_no
        self.cellphone = cellphone
    def requests(self):
        data = {
            "hsa_method": "tongdun.tongdun_loan_bodyguard",
            "hsa_version": "v1.0.0",
            "full_name": self.full_name,
            "id_no": self.id_no,
            "cellphone": self.cellphone,
            "hsa_account_code": "hshc_zhangxl",
            "hsa_account_key": "fff68e025c8743e14bbe398eaaee8ae6",
            "hsa_business_no": "1234567"
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