import numpy as np
import json
import requests
import datetime
from bs4 import BeautifulSoup
from akamx.sanfangshuju import Datas
def shijian(times):
    a1 = times.replace('年','-')
    a2 = a1.replace('月','-')
    a3 = a2.replace('日','')
    today = datetime.datetime.today()
    timness = datetime.datetime.strptime(a3,'%Y-%m-%d')
    timedte = (today-timness).days
    return timedte,timness




import datetime
today = datetime.datetime.today()
a = today.strftime("%Y-%m-%d %H:%M:%S")
b = a.replace('-','')
c =b.replace(':','')
d = c.replace(' ','')

class Reople:
    def __init__(self,full_name,id_no,cellphone,id_type):
        self.full_name =full_name
        self.id_no = id_no
        self.cellphone = cellphone
        self.id_type = id_type



    def loaninfo(self,ii):

        # ''' 贷款的字段  '''
        ###贷款最大逾期期数
        longestOverdueMonth = ''
        try:
            if 'oods' in json.loads(ii)['credit_result_json']['reportMessage'].keys():
                ###贷款最大逾期期数
                longestOverdueMonth = json.loads(ii)['credit_result_json']['reportMessage']['oods']['overdueLoan'][
                    'longestOverdueMonth']
            else:
                longestOverdueMonth = ''
        except:
            if 'oods' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                ###贷款最大逾期期数
                longestOverdueMonth = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['oods']['overdueLoan'][
                    'longestOverdueMonth']
            else:
                longestOverdueMonth = ''

        #print('longestOverdueMonth', longestOverdueMonth)

        ####
        ##近12个月贷款当前逾期总金额
        list_yuqu_12 = [0]
        #近6个月逾期额度
        list_currentOverdueAmount_6 = [0]
        # 近三个月贷款笔数
        list_num_3 = []
        ###贷款当前最大逾期期数
        list_yue = [0]
        ###贷款余额
        principalAmount_list = [0]
        ### 贷款总金额
        amount_list = [0.01]
        ### 贷款笔数
        len_bishu = []

        ###贷款24个月还款情况
        list_loan_yuqi = []
        try:
            if 'loanInfo' in json.loads(ii)['credit_result_json']['reportMessage'].keys():
                loanInfo = json.loads(ii)['credit_result_json']['reportMessage']['loanInfo']

                for lt in loanInfo:
                    if 'currentOverdueAmount' in lt.keys():
                        accountStatus = lt['accountStatus']
                        currentOverdueAmount = lt['currentOverdueAmount']
                        beginDate = lt['titleInfoObject']['beginDate']
                        currentOverdueNum = lt['currentOverdueNum']
                        principalAmount = lt['principalAmount'].replace(',', '')
                        principalAmount = float(principalAmount)
                        principalAmount_list.append(principalAmount)
                        amount = lt['titleInfoObject']['amount'].replace(',', '')
                        amount = float(amount)
                        amount_list.append(amount)
                        list_yue.append(currentOverdueNum)

                        ###贷款逾期期数
                        month24RepayStatus = lt['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])

                        list_loan_yuqi.append(month24RepayStatus_maax)

                        timedte, timness = shijian(beginDate)
                        if timedte < 12 * 30:
                            currentOverdueAmount = currentOverdueAmount
                            list_yuqu_12.append(currentOverdueAmount)
                            print('1111111111', accountStatus, timedte, timness, currentOverdueAmount=currentOverdueAmount)
                        ## 6个月的
                        if timedte < 6 * 30:
                            list_currentOverdueAmount_6.append(currentOverdueAmount)
                        if timedte < 3 * 30:
                            list_num_3.append(beginDate)
                        if timedte < 31:
                            len_bishu.append(beginDate)
                # print('list_yuqu',list_yuqu)
                # print('list_yue',list_yue)
                # print('zzzzzzzzzzzzzzzzzzzzzzzzzzz',sum(principalAmount_list)/sum(amount_list)*100)
                ###每笔贷款的最长逾期期数

            else:
                loanInfo = ''
        except:

            if 'loanInfo' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                loanInfo = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['loanInfo']

                for lt in loanInfo:
                    if 'currentOverdueAmount' in lt.keys():
                        accountStatus = lt['accountStatus']
                        print('accountStatusaccountStatusaccountStatus', accountStatus)
                        currentOverdueAmount = lt['currentOverdueAmount']
                        currentOverdueNum = lt['currentOverdueNum']
                        list_yue.append(currentOverdueNum)
                        principalAmount = lt['principalAmount'].replace(',', '')
                        principalAmount = float(principalAmount)
                        principalAmount_list.append(principalAmount)
                        amount = lt['titleInfoObject']['amount'].replace(',', '')
                        amount = float(amount)
                        amount_list.append(amount)

                        ###贷款逾期期数
                        month24RepayStatus = lt['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('D', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])

                        list_loan_yuqi.append(month24RepayStatus_maax)

                        beginDate = lt['titleInfoObject']['beginDate']
                        timedte, timness = shijian(beginDate)
                        ##12个月的
                        if timedte < 12 * 30:
                            currentOverdueAmount = currentOverdueAmount
                            list_yuqu_12.append(currentOverdueAmount)
                            print('22222222222222', accountStatus, timedte, timness, currentOverdueAmount)
                        ## 6个月的
                        if timedte < 6 * 30:
                            list_currentOverdueAmount_6.append(currentOverdueAmount)
                        if timedte < 3 * 30:
                            list_num_3.append(beginDate)
                        if timedte < 31:
                            len_bishu.append(beginDate)
        print('wwwwwwwwww', list_yuqu_12, list_yue, principalAmount_list, amount_list, len_bishu, list_loan_yuqi)
        return longestOverdueMonth,list_yuqu_12, list_yue, principalAmount_list, amount_list, len_bishu, list_loan_yuqi,list_num_3,list_currentOverdueAmount_6

        # """ 贷记卡"""
    def creditCardInfo(self,ii):
        # 使用额度
        list_usedMmount_djk = []
        # 额度
        list_usedMmount_amount_djk = []
        ## 逾期最大值
        list_djk_yuqi = [0]

        ## 使用额度比例
        rate_djk = []
        ##连续逾期
        djk_yuqi = []
        ## 6个月额度
        djk_six_amount = []
        ## 6个月使用额度
        djk_six_usedMmount = []
        ### 六个月使用率
        rate_six_djk = []
        ## 12个月的额度使用率
        rate_12_djk = [0]
        try:
            if 'creditCardInfo' in json.loads(ii)['credit_result_json']['reportMessage'].keys():
                creditCardInfo = json.loads(ii)['credit_result_json']['reportMessage']['creditCardInfo']

                for cd in creditCardInfo:
                    if 'usedMmount' in cd.keys():
                        usedMmount_djk = cd['usedMmount'].replace(',', '')
                        usedMmount_djk = float(usedMmount_djk)
                        list_usedMmount_djk.append(usedMmount_djk)

                        amount_djk = cd['titleInfoObject']['amount'].replace(',', '')

                        amount_djk = float(amount_djk)
                        if amount_djk == 0:
                            amount_djk = 0.001
                        else:
                            amount_djk = amount_djk
                        list_usedMmount_amount_djk.append(amount_djk)

                        rate_amout = usedMmount_djk / amount_djk
                        rate_djk.append(rate_amout)

                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])

                        list_djk_yuqi.append(month24RepayStatus_maax)
                        #print('month24RepayStatus', month24RepayStatus_maax)

                        beginDate = cd['titleInfoObject']['beginDate']
                        timedte, timness = shijian(beginDate)
                        if timedte < 6 * 30:
                            djk_six_amount.append(amount_djk)
                            djk_six_usedMmount.append(usedMmount_djk)
                            rate_six_djk.append(rate_amout)
                        if timedte < 12 * 30:
                            djk_six_amount.append(amount_djk)
                            djk_six_usedMmount.append(usedMmount_djk)
                            rate_12_djk.append(rate_djk)

        except:

            if 'creditCardInfo' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                creditCardInfo = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['creditCardInfo']

                for cd in creditCardInfo:
                    if 'usedMmount' in cd.keys():
                        usedMmount_djk = cd['usedMmount'].replace(',', '')
                        usedMmount_djk = float(usedMmount_djk)
                        list_usedMmount_djk.append(usedMmount_djk)

                        amount_djk = cd['titleInfoObject']['amount'].replace(',', '')
                        amount_djk = float(amount_djk)
                        if amount_djk == 0:
                            amount_djk = 0.001
                        else:
                            amount_djk = amount_djk
                        list_usedMmount_amount_djk.append(amount_djk)

                        rate_amout = usedMmount_djk / amount_djk
                        rate_djk.append(rate_amout)

                        month24RepayStatus = cd['month24RepayStatus']
                        month24RepayStatus1 = month24RepayStatus.replace('N', '0')
                        month24RepayStatus2 = month24RepayStatus1.replace('*', '0')
                        month24RepayStatus3 = month24RepayStatus2.replace('/', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('#', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('C', '0')
                        month24RepayStatus3 = month24RepayStatus3.replace('G', '0')
                        month24RepayStatus4 = month24RepayStatus3.split(' ')
                        month24RepayStatus_maax = max([float(x) for x in month24RepayStatus4])
                        djk_yuqi.append(month24RepayStatus_maax)
                        #print('month24RepayStatus', month24RepayStatus_maax)
                        beginDate = cd['titleInfoObject']['beginDate']

                        timedte, timness = shijian(beginDate)
                        if timedte < 6 * 30:
                            djk_six_amount.append(amount_djk)
                            djk_six_usedMmount.append(usedMmount_djk)
                            rate_six_djk.append(rate_amout)
                        if timedte < 12 * 30:
                            djk_six_amount.append(amount_djk)
                            djk_six_usedMmount.append(usedMmount_djk)
                            rate_12_djk.append(rate_djk)
        print('qqqqk', list_usedMmount_djk, list_usedMmount_amount_djk, list_djk_yuqi, rate_djk, djk_yuqi, djk_six_amount,
              djk_six_usedMmount, rate_six_djk)
        return list_usedMmount_djk, list_usedMmount_amount_djk, list_djk_yuqi, rate_djk, djk_yuqi, djk_six_amount,djk_six_usedMmount, rate_six_djk,rate_12_djk



    def queryRecordSum(self,ii):
        ###查询
        last1MonthsCreditCardApprovalSum = ''
        last1MonthsLoanApprovalSum = ''
        try:
            if 'queryRecordSum' in json.loads(ii)['credit_result_json']['reportMessage'].keys():
                last1MonthsCreditCardApprovalSum = json.loads(ii)['credit_result_json']['reportMessage']['queryRecordSum'][
                    'last1MonthsCreditCardApprovalSum']
                last1MonthsLoanApprovalSum = json.loads(ii)['credit_result_json']['reportMessage']['queryRecordSum'][
                    'last1MonthsLoanApprovalSum']
        except:

            if 'queryRecordSum' in json.loads(json.loads(ii)['statusMsg'])['reportMessage'].keys():
                last1MonthsCreditCardApprovalSum = \
                json.loads(json.loads(ii)['statusMsg'])['reportMessage']['queryRecordSum'][
                    'last1MonthsCreditCardApprovalSum']
                last1MonthsLoanApprovalSum = json.loads(json.loads(ii)['statusMsg'])['reportMessage']['queryRecordSum'][
                    'last1MonthsLoanApprovalSum']
        print(last1MonthsCreditCardApprovalSum, last1MonthsLoanApprovalSum)
        return last1MonthsCreditCardApprovalSum, last1MonthsLoanApprovalSum




    def renhanghongxian(self):
        ii = Datas(self.full_name, self.id_no, self.cellphone, self.id_type).pboc()
        longestOverdueMonth, list_yuqu_12, list_yue, principalAmount_list, amount_list, len_bishu, list_loan_yuqi,list_num_3,list_currentOverdueAmount_6 = self.loaninfo(ii)
        list_usedMmount_djk, list_usedMmount_amount_djk, list_djk_yuqi, rate_djk, djk_yuqi, djk_six_amount, djk_six_usedMmount, rate_six_djk ,rate_12_djk \
            = self.creditCardInfo(ii)
        last1MonthsCreditCardApprovalSum, last1MonthsLoanApprovalSum = self.queryRecordSum(ii)

        dict_credit_group = {}
        dict_credit_child = {}
        # PBOC001-贷款最大逾期期数>3且近3个月贷款笔数>10
        loan_max_overdue_terms = longestOverdueMonth
        loan_3month_num = sum(list_num_3)
        if loan_max_overdue_terms > 3 and loan_3month_num > 10:
            dict_credit_child['PBOC001'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC001'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC002-贷款最大逾期期数>3且信用卡审批查询次数>10
        # 信用卡审批查询次数
        card_query_num = last1MonthsCreditCardApprovalSum
        if loan_max_overdue_terms > 3 and card_query_num > 10:
            dict_credit_child['PBOC002'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC002'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC003-贷款最大逾期期数>3且近6个月贷款当前逾期最大金额>=1000
        # 近6个月贷款当前逾期最大金额>=1000

        loan_6month_current_overdue_max_amount = max(list_currentOverdueAmount_6)
        if loan_max_overdue_terms > 3 and loan_6month_current_overdue_max_amount > 1000:
            dict_credit_child['PBOC003'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC003'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC004-贷款最大逾期期数>3且近6个月贷记卡最大额度使用率>0.5
        card_6month_max_used_rate = max(rate_six_djk)
        if loan_max_overdue_terms > 3 and card_6month_max_used_rate > 0.5:
            dict_credit_child['PBOC004'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC004'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC005-近12个月贷款当前逾期总金额>3000且近3个月贷款笔数>3
        loan_12month_current_overdue_sum_amount = sum(list_yuqu_12)
        loan_3month_num = len(list_num_3)

        if loan_12month_current_overdue_sum_amount > 3000 and loan_3month_num > 3:
            dict_credit_child['PBOC005'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC005'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC006-近12个月贷款当前逾期总金额>3000且近6个月平均使用额度的总和>10000
        card_6month_average_amount = np.mean(djk_six_usedMmount)
        if loan_12month_current_overdue_sum_amount > 3000 and card_6month_average_amount > 10000:
            dict_credit_child['PBOC006'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC006'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC007-近12个月贷款当前逾期总金额>3000且贷款最大逾期期数>3
        if loan_12month_current_overdue_sum_amount > 3000 and loan_max_overdue_terms > 3:
            dict_credit_child['PBOC007'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC007'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC008-近12个月贷款当前逾期总金额>3000且贷记卡连续逾期月份数>3
        card_overdue_terms = max(list_loan_yuqi)
        if loan_12month_current_overdue_sum_amount > 3000 and card_overdue_terms > 3:
            dict_credit_child['PBOC008'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC008'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC009-近12个月贷款当前逾期总金额>3000且贷款审批查询次数>20
        loan_query_num = last1MonthsLoanApprovalSum
        if loan_12month_current_overdue_sum_amount > 3000 and loan_query_num > 20:
            dict_credit_child['PBOC009'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC009'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC010-近12个月贷款当前逾期总金额>5000且贷款总逾期次数>10

        loan_overdue_num = len(list_yue)
        if loan_12month_current_overdue_sum_amount > 5000 and loan_overdue_num > 10:
            dict_credit_child['PBOC010'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC010'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC011-贷款当前最大逾期期数>1且近12个月贷记卡最小额度使用率>0.5
        card_12month_min_used_rate = min(rate_12_djk)
        loan_current_max_overdue_terms =max(list_yue)
        if loan_current_max_overdue_terms > 1 and card_12month_min_used_rate > 0.5:
            dict_credit_child['PBOC011'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC011'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC012-贷款当前最大逾期期数>1且贷记卡总的已使用额度>100000
        card_used_sum_amount = sum(list_usedMmount_djk)

        if loan_current_max_overdue_terms > 1 and card_used_sum_amount > 100000:
            dict_credit_child['PBOC012'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC012'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC013-贷款当前最大逾期期数>1且贷款拒绝次数>10
        loan_refuse_num = last1MonthsLoanApprovalSum - len(len_bishu)
        if loan_current_max_overdue_terms > 1 and loan_refuse_num > 10:
            dict_credit_child['PBOC013'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC013'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC014-贷款当前最大逾期期数>1且近6个月贷款当前逾期总金额>10000
        loan_6month_current_overdue_sum_amount = sum(list_currentOverdueAmount_6)
        if loan_current_max_overdue_terms > 1 and loan_6month_current_overdue_sum_amount > 10000:
            dict_credit_child['PBOC014'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC014'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC015-贷款当前最大逾期期数>1且信用卡审批查询次数>20
        loan_current_max_overdue_terms = max(list_yue)

        if loan_current_max_overdue_terms > 1 and card_query_num > 20:
            dict_credit_child['PBOC015'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC015'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC016-贷款当前最大逾期期数>5且贷款余额占总金额比率>0.9
        loan_balance_rate = sum(principalAmount_list) / sum(amount_list)
        if loan_current_max_overdue_terms > 5 and loan_balance_rate > 0.9:
            dict_credit_child['PBOC016'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC016'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC017-贷款审批查询次数>10且贷记卡最大逾期期数>3
        card_max_overdue_terms = max(list_djk_yuqi)
        if loan_query_num > 10 and card_max_overdue_terms > 3:
            dict_credit_child['PBOC017'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC017'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC018-贷款审批查询次数>10且贷记卡当前逾期期数大于0的账户数>2
        card_current_overdue_num = len(list_djk_yuqi)
        if loan_query_num > 10 and card_current_overdue_num > 2:
            dict_credit_child['PBOC018'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC018'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC019-贷款审批查询次数>10且贷款最大逾期期数>5

        if loan_query_num > 10 and loan_max_overdue_terms > 5:
            dict_credit_child['PBOC019'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC019'] = 0
            dict_credit_group.update(dict_credit_child)
        # PBOC020-贷记卡当前逾期期数大于0的账户数>2且贷记卡最大逾期期数>5
        [x for x in list_djk_yuqi if x > 0]
        card_current_overdue_terms = list_djk_yuqi
        if card_current_overdue_terms > 2 and card_max_overdue_terms > 5:
            dict_credit_child['PBOC020'] = 1
            dict_credit_group.update(dict_credit_child)
        else:
            dict_credit_child['PBOC020'] = 0
            dict_credit_group.update(dict_credit_child)
        return dict_credit_group ,dict_credit_child
