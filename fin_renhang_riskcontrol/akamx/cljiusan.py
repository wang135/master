

class Cl_score:
    # def __init__(self):
    def cl_score(self,allcl):
        #---------------------------------------------------A卡模型策略规则---------------------------------------------------#
        dict_strategy_group = {}
        dict_stratege_child = {}
        dict_stratege_child_br = {}
        dict_strategy_group_br = {}
        #---------------------------------------------------同盾策略规则---------------------------------------------------#
        if allcl['i_freq_policy_Review_all_all_60day'] >= 19.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0001'] = 88
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0001'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_90day'] >= 3.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0002'] = 85
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0002'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0003'] = 85
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0003'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_90day'] >= 3.5 and allcl['m_cnt_partner_last2ndmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0004'] = 84
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0004'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 11.5 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0005'] = 84
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0005'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_60day'] >= 2.5 and allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0006'] = 84
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0006'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['m_cnt_partner_last5thmth_Loan_all_365day'] >=9.5 :
            dict_stratege_child['TD0007'] = 84
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0007'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['i_freq_policy_Reject_all_all_180day'] >=30.5 :
            dict_stratege_child['TD0008'] = 83
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0008'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['m_pctl_cnt_ic_partner_Loan_Bank_365day'] >=0.419 :
            dict_stratege_child['TD0009'] = 82
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0009'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_90day'] >= 29.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0010'] = 82
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0010'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_30day'] >= 12.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0011'] = 82
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0011'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 11.5 and allcl['m_cnt_node_dist1_Loan_all_all'] >=4.5 :
            dict_stratege_child['TD0012'] = 82
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0012'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >= 1.5 and allcl['i_cnt_partner_last5thmth_Loan_IFinanceWeb_365day'] >=0.5 :
            dict_stratege_child['TD0013'] = 82
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0013'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 2.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0014'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0014'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_all_90day'] >= 5.5 and allcl['i_freq_policy_Review_all_all_180day'] >=51.5 :
            dict_stratege_child['TD0015'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0015'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Offloan_90day'] >= 1.5 and allcl['i_pctl_cnt_ic_partner_Loan_Bank_180day'] >=0.483 :
            dict_stratege_child['TD0016'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0016'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >=0.5 :
            dict_stratege_child['TD0017'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0017'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_P2pweb_90day'] >= 3.5 and allcl['i_freq_policy_Review_all_all_60day'] >=19.5 :
            dict_stratege_child['TD0018'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0018'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_finance_60day'] >= 4.5 and allcl['m_cnt_node_reject_Loan_all_all'] >=11.5 :
            dict_stratege_child['TD0019'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0019'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_90day'] >= 3.5 and allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >=0.012 :
            dict_stratege_child['TD0020'] = 81
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0020'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 6.5 and allcl['i_cnt_partner_last3rdmth_Loan_Insurance_365day'] >=0.5 :
            dict_stratege_child['TD0021'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0021'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['m_cnt_node_dist1_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0022'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0022'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_finance_365day'] >= 7.5 and allcl['m_freq_policy_Accept_all_all_60day'] >=73.5 :
            dict_stratege_child['TD0023'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0023'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_90day'] >= 31.5 and allcl['i_max_cnt_partner_daily_Loan_finance_180day'] >=5.5 :
            dict_stratege_child['TD0024'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0024'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >= 0.793 and allcl['m_max_cnt_partner_daily_Loan_Consumerfinance_365day'] >=1.5 :
            dict_stratege_child['TD0025'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0025'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 6.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.001 :
            dict_stratege_child['TD0026'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0026'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_finance_60day'] >= 2.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.016 :
            dict_stratege_child['TD0027'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0027'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_30day'] >= 3.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0028'] = 80
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0028'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 5.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.001 :
            dict_stratege_child['TD0029'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0029'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last6thmth_Loan_all_365day'] >= 8.5 and allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_365day'] >=1.5 :
            dict_stratege_child['TD0030'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0030'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_60day'] >= 20.5 and allcl['i_freq_policy_Reject_all_all_365day'] >=29.5 :
            dict_stratege_child['TD0031'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0031'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_90day'] >= 2.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0032'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0032'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_finance_90day'] >= 5.5 and allcl['i_freq_policy_Reject_all_all_365day'] >=29.5 :
            dict_stratege_child['TD0033'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0033'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_365day'] >= 2.5 and allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >=0.012 :
            dict_stratege_child['TD0034'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0034'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_60day'] >= 20.5 and allcl['m_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0035'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0035'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_finance_180day'] >= 5.5 and allcl['m_freq_policy_Review_all_all_180day'] >=46.5 :
            dict_stratege_child['TD0036'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0036'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_all_60day'] >= 4.5 and allcl['m_ratio_cnt_grp_mobile_Loan_all_all'] >=0.789 :
            dict_stratege_child['TD0037'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0037'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_all_30day'] >= 4.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0038'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0038'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 1.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0039'] = 79
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0039'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last3rdmth_Loan_Imbank_365day'] >= 5.5 and allcl['m_cnt_partner_last2ndmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0040'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0040'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_finance_365day'] >= 7.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.021 :
            dict_stratege_child['TD0041'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0041'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_365day'] >=1.5 :
            dict_stratege_child['TD0042'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0042'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Offloan_365day'] >= 1.5 and allcl['m_pctl_cnt_ic_partner_Loan_Bank_180day'] >=0.62 :
            dict_stratege_child['TD0043'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0043'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_30day'] >= 5.5 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.622 :
            dict_stratege_child['TD0044'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0044'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 11.5 and allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >=0.118 :
            dict_stratege_child['TD0045'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0045'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 3.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.016 :
            dict_stratege_child['TD0046'] = 78
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0046'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Imbank_60day'] >= 5.5 and allcl['m_max_cnt_partner_daily_Loan_P2pweb_60day'] >=2.5 :
            dict_stratege_child['TD0047'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0047'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 1.5 and allcl['m_freq_policy_Accept_all_all_180day'] >=208.5 :
            dict_stratege_child['TD0048'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0048'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_pctl_cnt_ic_partner_Loan_Imbank_90day'] >= 0.787 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0049'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0049'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_90day'] >= 5.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.016 :
            dict_stratege_child['TD0050'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0050'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 30.5 and allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >=0.5 :
            dict_stratege_child['TD0051'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0051'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 2.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.016 :
            dict_stratege_child['TD0052'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0052'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_90day'] >= 2.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_180day'] >=0.533 :
            dict_stratege_child['TD0053'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0053'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 1.5 and allcl['m_cnt_partner_last2ndmth_Loan_Bank_365day'] >=1.5 :
            dict_stratege_child['TD0054'] = 77
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0054'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_60day'] >= 20.5 and allcl['m_cnt_node_partner_Loan_all_all'] >=12.5 :
            dict_stratege_child['TD0055'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0055'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last4thmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['m_max_cnt_partner_daily_Loan_con_30day'] >=1.5 :
            dict_stratege_child['TD0056'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0056'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_180day'] >= 0.533 and allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >=0.012 :
            dict_stratege_child['TD0057'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0057'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 30.5 and allcl['i_freq_policy_Review_all_all_60day'] >=13.5 :
            dict_stratege_child['TD0058'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0058'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Bank_365day'] >= 0.797 and allcl['m_max_cnt_partner_daily_Loan_finance_60day'] >=2.5 :
            dict_stratege_child['TD0059'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0059'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=2.5 :
            dict_stratege_child['TD0060'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0060'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 1.5 and allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >=0.012 :
            dict_stratege_child['TD0061'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0061'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_all_365day'] >= 7.5 and allcl['m_max_cnt_partner_daily_Loan_Unconsumerfinance_365day'] >=2.5 :
            dict_stratege_child['TD0062'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0062'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.771 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0063'] = 76
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0063'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Imbank_365day'] >= 9.5 and allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >=0.118 :
            dict_stratege_child['TD0064'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0064'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['m_max_cnt_partner_daily_Loan_all_30day'] >=2.5 :
            dict_stratege_child['TD0065'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0065'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 3.5 and allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >=0.118 :
            dict_stratege_child['TD0066'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0066'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_30day'] >= 1.5 and allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >=0.31 :
            dict_stratege_child['TD0067'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0067'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_60day'] >= 19.5 and allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_60day'] >=1.5 :
            dict_stratege_child['TD0068'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0068'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 5.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >=0.578 :
            dict_stratege_child['TD0069'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0069'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_365day'] >= 29.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0070'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0070'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_180day'] >= 3.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0071'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0071'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_90day'] >= 2.5 and allcl['m_max_cnt_partner_daily_Loan_P2pweb_30day'] >=1.5 :
            dict_stratege_child['TD0072'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0072'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['m_freq_policy_Accept_all_all_90day'] >=114.5 :
            dict_stratege_child['TD0073'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0073'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_60day'] >= 9.5 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0074'] = 75
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0074'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 11.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_30day'] >=2.5 :
            dict_stratege_child['TD0075'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0075'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['i_cnt_partner_last6thmth_Loan_Imbank_365day'] >=4.5 :
            dict_stratege_child['TD0076'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0076'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_180day'] >= 2.5 and allcl['m_cnt_node_partner_Loan_all_all'] >=12.5 :
            dict_stratege_child['TD0077'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0077'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_365day'] >= 2.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >=0.284 :
            dict_stratege_child['TD0078'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0078'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_get_node_rank_value_Loan_all_all'] >= 0.016 and allcl['m_freq_policy_Reject_all_all_60day'] >=0.5 :
            dict_stratege_child['TD0079'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0079'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 1.5 and allcl['i_freq_policy_Reject_all_all_60day'] >=0.5 :
            dict_stratege_child['TD0080'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0080'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_365day'] >= 29.5 and allcl['m_freq_policy_Reject_all_all_30day'] >=0.5 :
            dict_stratege_child['TD0081'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0081'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_180day'] >= 3.5 and allcl['m_cnt_node_dist2_device_Loan_all_all'] >=1.5 :
            dict_stratege_child['TD0082'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0082'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 5.5 and allcl['m_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0083'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0083'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_365day'] >= 29.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >=3.5 :
            dict_stratege_child['TD0084'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0084'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.771 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0085'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0085'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_60day'] >= 3.5 and allcl['i_freq_policy_Accept_all_all_60day'] >=50.5 :
            dict_stratege_child['TD0086'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0086'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 1.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0087'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0087'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last3rdmth_Loan_all_365day'] >= 4.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0088'] = 74
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0088'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['m_max_cnt_partner_daily_Loan_Imbank_30day'] >=1.5 :
            dict_stratege_child['TD0089'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0089'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_get_node_rank_value_Loan_all_all'] >= 0.016 and allcl['i_cnt_node_dist1_cmobile_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0090'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0090'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['i_cnt_partner_last2ndmth_Loan_Imbank_365day'] >=3.5 :
            dict_stratege_child['TD0091'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0091'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_freq_policy_Reject_all_all_60day'] >=2.5 :
            dict_stratege_child['TD0092'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0092'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_cnt_node_dist1_card_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0093'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0093'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_90day'] >= 0.759 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0094'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0094'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_30day'] >= 1.5 and allcl['m_cnt_node_dist1_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0095'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0095'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_node_dist1_device_Loan_all_all'] >= 1.5 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_60day'] >=0.22 :
            dict_stratege_child['TD0096'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0096'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 2.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >=0.284 :
            dict_stratege_child['TD0097'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0097'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 7.5 and allcl['m_freq_policy_Accept_all_all_90day'] >=114.5 :
            dict_stratege_child['TD0098'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0098'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 7.5 and allcl['m_max_cnt_partner_daily_Loan_Unconsumerfinance_60day'] >=1.5 :
            dict_stratege_child['TD0099'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0099'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_30day'] >= 5.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0100'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0100'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last2ndmth_Loan_all_365day'] >= 7.5 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.521 :
            dict_stratege_child['TD0101'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0101'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_365day'] >=1.5 :
            dict_stratege_child['TD0102'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0102'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_node_partner_Loan_all_all'] >= 12.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >=0.284 :
            dict_stratege_child['TD0103'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0103'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 2.5 and allcl['i_cnt_partner_last4thmth_Loan_all_365day'] >=7.5 :
            dict_stratege_child['TD0104'] = 73
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0104'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_180day'] >= 2.5 and allcl['m_cnt_partner_last5thmth_Loan_all_365day'] >=3.5 :
            dict_stratege_child['TD0105'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0105'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >=0.284 :
            dict_stratege_child['TD0106'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0106'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 5.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_180day'] >=3.5 :
            dict_stratege_child['TD0107'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0107'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0108'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0108'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0109'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0109'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Imbank_365day'] >= 3.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0110'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0110'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last5thmth_Loan_all_365day'] >= 3.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.748 :
            dict_stratege_child['TD0111'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0111'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_node_dist1_cmobile_Loan_all_all'] >= 4.5 and allcl['i_get_node_rank_value_Loan_all_all'] >=0.018 :
            dict_stratege_child['TD0112'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0112'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last3rdmth_Loan_Imbank_365day'] >= 5.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_180day'] >=3.5 :
            dict_stratege_child['TD0113'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0113'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 3.5 and allcl['m_freq_policy_Review_all_all_365day'] >=13.5 :
            dict_stratege_child['TD0114'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0114'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Bank_60day'] >= 0.673 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_60day'] >=0.588 :
            dict_stratege_child['TD0115'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0115'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_90day'] >= 3.5 and allcl['i_max_cnt_partner_daily_Loan_all_30day'] >=2.5 :
            dict_stratege_child['TD0116'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0116'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_180day'] >= 2.5 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.521 :
            dict_stratege_child['TD0117'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0117'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 7.5 and allcl['i_freq_policy_Accept_all_all_90day'] >=73.5 :
            dict_stratege_child['TD0118'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0118'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 5.5 and allcl['i_max_cnt_partner_daily_Loan_con_90day'] >=1.5 :
            dict_stratege_child['TD0119'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0119'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0120'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0120'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 5.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0121'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0121'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_cnt_node_partner_Loan_all_all'] >=10.5 :
            dict_stratege_child['TD0122'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0122'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 10.5 and allcl['i_freq_policy_Reject_all_all_30day'] >=1.5 :
            dict_stratege_child['TD0123'] = 72
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0123'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >= 0.118 and allcl['m_max_cnt_partner_daily_Loan_con_90day'] >=1.5 :
            dict_stratege_child['TD0124'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0124'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 2.5 and allcl['m_freq_policy_Accept_all_all_30day'] >=15.5 :
            dict_stratege_child['TD0125'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0125'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >= 0.167 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0126'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0126'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0127'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0127'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >= 0.012 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0128'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0128'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Unconsumerfinance_90day'] >= 1.5 and allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0129'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0129'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last3rdmth_Loan_all_365day'] >= 4.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_90day'] >=2.5 :
            dict_stratege_child['TD0130'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0130'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0131'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0131'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_90day'] >= 73.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.748 :
            dict_stratege_child['TD0132'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0132'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_IFinanceWeb_365day'] >= 0.5 and allcl['m_freq_policy_Reject_all_all_180day'] >=1.5 :
            dict_stratege_child['TD0133'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0133'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_365day'] >= 2.5 and allcl['i_freq_policy_Review_all_all_365day'] >=6.5 :
            dict_stratege_child['TD0134'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0134'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_30day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0135'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0135'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_con_30day'] >= 1.5 and allcl['m_ratio_cnt_node_reject_Loan_all_all'] >=0.129 :
            dict_stratege_child['TD0136'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0136'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.572 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0137'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0137'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_dist1_device_Loan_all_all'] >= 0.118 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0138'] = 71
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0138'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_pctl_cnt_ic_partner_Loan_Bank_180day'] >=0.637 :
            dict_stratege_child['TD0139'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0139'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 3.5 and allcl['i_freq_policy_Review_all_all_365day'] >=24.5 :
            dict_stratege_child['TD0140'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0140'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0141'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0141'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 1.5 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_30day'] >=0.505 :
            dict_stratege_child['TD0142'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0142'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Imbank_365day'] >= 3.5 and allcl['m_max_cnt_partner_daily_Loan_all_30day'] >=1.5 :
            dict_stratege_child['TD0143'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0143'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_180day'] >= 2.5 and allcl['i_freq_policy_Review_all_all_365day'] >=6.5 :
            dict_stratege_child['TD0144'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0144'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 1.5 and allcl['i_cnt_partner_last1stmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0145'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0145'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 5.5 and allcl['i_freq_policy_Reject_all_all_30day'] >=1.5 :
            dict_stratege_child['TD0146'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0146'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Accept_all_all_180day'] >= 208.5 and allcl['i_freq_policy_Accept_all_all_30day'] >=25.5 :
            dict_stratege_child['TD0147'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0147'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.578 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0148'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0148'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_60day'] >= 0.5 and allcl['m_get_node_rank_value_Loan_all_all'] >=0.001 :
            dict_stratege_child['TD0149'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0149'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_60day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_30day'] >=1.5 :
            dict_stratege_child['TD0150'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0150'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 1.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0151'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0151'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 2.5 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0152'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0152'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_30day'] >= 25.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0153'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0153'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 1.5 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >=0.167 :
            dict_stratege_child['TD0154'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0154'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_60day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0155'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0155'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last3rdmth_Loan_Imbank_365day'] >= 1.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.748 :
            dict_stratege_child['TD0156'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0156'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_30day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_con_90day'] >=1.5 :
            dict_stratege_child['TD0157'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0157'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_get_node_rank_value_Loan_all_all'] >= 0.018 and allcl['i_ratio_cnt_node_dist1_device_Loan_all_all'] >=0.095 :
            dict_stratege_child['TD0158'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0158'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_90day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_con_60day'] >=1.5 :
            dict_stratege_child['TD0159'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0159'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_node_dist2_Loan_all_all'] >= 19.5 and allcl['m_ratio_cnt_node_reject_Loan_all_all'] >=0.129 :
            dict_stratege_child['TD0160'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0160'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0161'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0161'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 3.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=1.5 :
            dict_stratege_child['TD0162'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0162'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Imbank_365day'] >= 3.5 and allcl['i_freq_policy_Accept_all_all_365day'] >=88.5 :
            dict_stratege_child['TD0163'] = 70
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0163'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_365day'] >= 24.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0164'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0164'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0165'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0165'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last6thmth_Loan_Imbank_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0166'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0166'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0167'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0167'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_30day'] >= 0.5 and allcl['m_ratio_cnt_grp_device_Loan_all_all'] >=0.057 :
            dict_stratege_child['TD0168'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0168'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Bank_90day'] >= 0.598 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.521 :
            dict_stratege_child['TD0169'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0169'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >= 0.748 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0170'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0170'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_cnt_partner_last1stmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0171'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0171'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0172'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0172'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >= 0.5 and allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >=0.092 :
            dict_stratege_child['TD0173'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0173'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 3.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0174'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0174'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_max_cnt_partner_daily_Loan_con_365day'] >=1.5 :
            dict_stratege_child['TD0175'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0175'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_365day'] >= 0.393 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0176'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0176'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0177'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0177'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0178'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0178'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_all_30day'] >= 1.5 and allcl['m_cnt_partner_last2ndmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0179'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0179'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_60day'] >= 0.5 and allcl['i_get_node_rank_value_Loan_all_all'] >=0.009 :
            dict_stratege_child['TD0180'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0180'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_dist2_id_Loan_all_all'] >= 0.012 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0181'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0181'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_60day'] >=1.5 :
            dict_stratege_child['TD0182'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0182'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_30day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0183'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0183'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_freq_policy_Reject_all_all_180day'] >=0.5 :
            dict_stratege_child['TD0184'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0184'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >= 0.5 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.755 :
            dict_stratege_child['TD0185'] = 69
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0185'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_180day'] >=0.5 :
            dict_stratege_child['TD0186'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0186'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >= 0.167 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0187'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0187'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last4thmth_Loan_Imbank_365day'] >= 1.5 and allcl['m_ratio_cnt_node_reject_Loan_all_all'] >=0.129 :
            dict_stratege_child['TD0188'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0188'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_90day'] >= 0.5 and allcl['m_freq_policy_Accept_all_all_60day'] >=31.5 :
            dict_stratege_child['TD0189'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0189'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_30day'] >= 25.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0190'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0190'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['m_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0191'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0191'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_90day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_30day'] >=0.5 :
            dict_stratege_child['TD0192'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0192'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >= 0.748 and allcl['m_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0193'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0193'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0194'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0194'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >= 0.5 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.755 :
            dict_stratege_child['TD0195'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0195'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_365day'] >= 24.5 and allcl['i_freq_policy_Accept_all_all_60day'] >=20.5 :
            dict_stratege_child['TD0196'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0196'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_device_Loan_all_all'] >= 0.057 and allcl['m_max_cnt_partner_daily_Loan_Offloan_180day'] >=0.5 :
            dict_stratege_child['TD0197'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0197'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0198'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0198'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >= 0.167 and allcl['i_max_cnt_partner_daily_Loan_Offloan_180day'] >=0.5 :
            dict_stratege_child['TD0199'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0199'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_30day'] >= 0.5 and allcl['m_cnt_node_dist1_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0200'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0200'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_30day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0201'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0201'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_180day'] >= 1.5 and allcl['i_cnt_partner_last6thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0202'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0202'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0203'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0203'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 0.5 and allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0204'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0204'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_device_Loan_all_all'] >= 0.057 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0205'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0205'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 1.5 and allcl['i_freq_policy_Review_all_all_365day'] >=6.5 :
            dict_stratege_child['TD0206'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0206'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last4thmth_Loan_Bank_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0207'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0207'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_30day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0208'] = 68
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0208'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 0.5 and allcl['i_freq_policy_Accept_all_all_365day'] >=88.5 :
            dict_stratege_child['TD0209'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0209'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Inconsumerfinance_90day'] >= 0.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0210'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0210'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_con_365day'] >=1.5 :
            dict_stratege_child['TD0211'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0211'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_30day'] >= 0.284 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_180day'] >=0.067 :
            dict_stratege_child['TD0212'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0212'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >= 0.748 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0213'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0213'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >= 2.5 and allcl['i_max_cnt_partner_daily_Loan_con_365day'] >=1.5 :
            dict_stratege_child['TD0214'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0214'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Imbank_180day'] >= 1.5 and allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0215'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0215'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >=0.5 :
            dict_stratege_child['TD0216'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0216'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_180day'] >= 0.067 and allcl['i_is_core_node_Loan_all_all'] >=0.5 :
            dict_stratege_child['TD0217'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0217'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_30day'] >= 3.5 and allcl['m_freq_policy_Accept_all_all_30day'] >=4.5 :
            dict_stratege_child['TD0218'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0218'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 0.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0219'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0219'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last2ndmth_Loan_Imbank_365day'] >= 1.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0220'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0220'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Accept_all_all_60day'] >= 31.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0221'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0221'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >=1.5 :
            dict_stratege_child['TD0222'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0222'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last2ndmth_Loan_Bank_365day'] >= 0.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0223'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0223'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Imbank_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_con_365day'] >=1.5 :
            dict_stratege_child['TD0224'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0224'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_30day'] >= 0.5 and allcl['i_freq_policy_Reject_all_all_60day'] >=0.5 :
            dict_stratege_child['TD0225'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0225'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Bank_180day'] >= 0.637 and allcl['i_pctl_cnt_ic_partner_Loan_Bank_365day'] >=0.401 :
            dict_stratege_child['TD0226'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0226'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_60day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0227'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0227'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_node_dist1_Loan_all_all'] >= 7.5 and allcl['i_ratio_cnt_node_reject_Loan_all_all'] >=0.063 :
            dict_stratege_child['TD0228'] = 67
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0228'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_30day'] >= 0.5 and allcl['i_freq_policy_Accept_all_all_365day'] >=23.5 :
            dict_stratege_child['TD0229'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0229'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last3rdmth_Loan_Bank_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0230'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0230'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 0.5 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.755 :
            dict_stratege_child['TD0231'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0231'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_reject_Loan_all_all'] >= 0.129 and allcl['m_ratio_cnt_node_review_Loan_all_all'] >=0.335 :
            dict_stratege_child['TD0232'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0232'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Unconsumerfinance_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_con_365day'] >=1.5 :
            dict_stratege_child['TD0233'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0233'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >= 0.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0234'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0234'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0235'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0235'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_finance_90day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0236'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0236'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_pctl_cnt_ic_partner_Loan_Imbank_60day'] >= 0.167 and allcl['i_pctl_cnt_ic_partner_Loan_Imbank_180day'] >=0.067 :
            dict_stratege_child['TD0237'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0237'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_get_node_rank_value_Loan_all_all'] >= 0.001 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0238'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0238'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_90day'] >= 2.5 and allcl['i_freq_policy_Accept_all_all_90day'] >=28.5 :
            dict_stratege_child['TD0239'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0239'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_180day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0240'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0240'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_device_Loan_all_all'] >= 0.057 and allcl['m_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0241'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0241'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >=0.5 :
            dict_stratege_child['TD0242'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0242'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >= 0.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0243'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0243'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_ratio_cnt_node_dist1_device_Loan_all_all'] >= 0.054 and allcl['i_cnt_node_dist1_mobile_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0244'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0244'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_Offloan_180day'] >= 0.5 and allcl['m_freq_policy_Review_all_all_60day'] >=0.5 :
            dict_stratege_child['TD0245'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0245'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >= 0.509 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_60day'] >=0.22 :
            dict_stratege_child['TD0246'] = 66
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0246'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_180day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0247'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0247'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_node_dist1_Loan_all_all'] >= 7.5 and allcl['i_cnt_node_dist2_id_Loan_all_all'] >=2.5 :
            dict_stratege_child['TD0248'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0248'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Reject_all_all_60day'] >= 0.5 and allcl['m_freq_policy_Reject_all_all_180day'] >=0.5 :
            dict_stratege_child['TD0249'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0249'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_dist2_device_Loan_all_all'] >= 0.092 and allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >=0.521 :
            dict_stratege_child['TD0250'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0250'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Accept_all_all_30day'] >= 15.5 and allcl['m_freq_policy_Accept_all_all_90day'] >=33.5 :
            dict_stratege_child['TD0251'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0251'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_60day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0252'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0252'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_365day'] >= 23.5 and allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >=0.509 :
            dict_stratege_child['TD0253'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0253'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0254'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0254'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_365day'] >= 23.5 and allcl['m_pctl_cnt_ic_partner_Loan_Imbank_60day'] >=0.22 :
            dict_stratege_child['TD0255'] = 65
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0255'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Reject_all_all_180day'] >= 0.5 and allcl['i_freq_policy_Review_all_all_180day'] >=0.5 :
            dict_stratege_child['TD0256'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0256'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_60day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0257'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0257'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_con_365day'] >= 1.5 and allcl['i_max_cnt_partner_daily_Loan_Imbank_365day'] >=1.5 :
            dict_stratege_child['TD0258'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0258'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >= 0.5 and allcl['i_freq_policy_Accept_all_all_365day'] >=23.5 :
            dict_stratege_child['TD0259'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0259'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Offloan_90day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Offloan_180day'] >=0.5 :
            dict_stratege_child['TD0260'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0260'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Review_all_all_30day'] >= 0.5 and allcl['i_freq_policy_Review_all_all_180day'] >=0.5 :
            dict_stratege_child['TD0261'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0261'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >= 0.521 and allcl['m_ratio_cnt_node_reject_Loan_all_all'] >=0.129 :
            dict_stratege_child['TD0262'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0262'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 0.5 and allcl['m_ratio_cnt_node_review_Loan_all_all'] >=0.335 :
            dict_stratege_child['TD0263'] = 64
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0263'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_freq_policy_Review_all_all_60day'] >= 0.5 and allcl['m_freq_policy_Accept_all_all_30day'] >=4.5 :
            dict_stratege_child['TD0264'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0264'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 0.5 and allcl['m_max_cnt_partner_daily_Loan_P2pweb_180day'] >=0.5 :
            dict_stratege_child['TD0265'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0265'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_P2pweb_180day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0266'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0266'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last1stmth_Loan_Bank_365day'] >= 0.5 and allcl['m_cnt_partner_last1stmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0267'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0267'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_cnt_partner_last5thmth_Loan_Bank_365day'] >= 0.5 and allcl['m_cnt_partner_last5thmth_Loan_Bank_365day'] >=0.5 :
            dict_stratege_child['TD0268'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0268'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_grp_reject_review_Loan_all_all'] >= 0.509 and allcl['m_ratio_cnt_node_review_Loan_all_all'] >=0.335 :
            dict_stratege_child['TD0269'] = 63
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0269'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_90day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0270'] = 62
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0270'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_freq_policy_Accept_all_all_30day'] >= 4.5 and allcl['i_freq_policy_Accept_all_all_365day'] >=23.5 :
            dict_stratege_child['TD0271'] = 62
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0271'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_ratio_cnt_node_reject_review_Loan_all_all'] >= 0.521 and allcl['m_ratio_cnt_node_review_Loan_all_all'] >=0.335 :
            dict_stratege_child['TD0272'] = 62
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0272'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['m_max_cnt_partner_daily_Loan_P2pweb_365day'] >= 0.5 and allcl['i_max_cnt_partner_daily_Loan_P2pweb_365day'] >=0.5 :
            dict_stratege_child['TD0273'] = 62
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0273'] = 0
            dict_strategy_group.update(dict_stratege_child)
        if allcl['i_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >= 0.5 and allcl['m_max_cnt_partner_daily_Loan_Consumerfinance_180day'] >=0.5 :
            dict_stratege_child['TD0274'] = 61
            dict_strategy_group.update(dict_stratege_child)
        else:
            dict_stratege_child['TD0274'] = 0
            dict_strategy_group.update(dict_stratege_child)

        #---------------------------------------------------百融策略规则---------------------------------------------------#
            #---------------------------------------------------百融策略规则---------------------------------------------------#

        if allcl['ir_m6_cell_x_tel_home_cnt'] >= 4.0 or allcl['ir_m6_cell_x_biz_addr_cnt'] >= 4.0 or allcl[
            'ir_m6_cell_x_home_addr_cnt'] >= 4.0 or allcl['ir_m6_cell_x_id_cnt'] >= 3.0 or allcl[
            'ir_m6_cell_x_mail_cnt'] >= 4.0:
            dict_stratege_child_br['BR0001'] = 60
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0001'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_max_monnum'] >= 17.0 or allcl['als_m12_id_max_monnum'] >= 17.0:
            dict_stratege_child_br['BR0002'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0002'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_caon_allnum'] >= 5.0 or allcl['als_m1_id_caon_allnum'] >= 5.0:
            dict_stratege_child_br['BR0003'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0003'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_max_monnum'] >= 13.0 or allcl['als_m12_cell_max_monnum'] >= 13.0:
            dict_stratege_child_br['BR0004'] = 76
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0004'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_nbank_week_allnum'] >= 4.0 or allcl['als_m12_cell_nbank_week_allnum'] >= 11.0 or allcl[
            'als_m1_id_nbank_week_allnum'] >= 4.0 or allcl['als_m12_id_nbank_week_allnum'] >= 11.0:
            dict_stratege_child_br['BR0005'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0005'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_caon_allnum'] >= 3.0 or allcl['als_m1_id_caon_allnum'] >= 3.0:
            dict_stratege_child_br['BR0006'] = 76
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0006'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['ex_bad1_name'] != -111 and allcl['ex_bad1_performance'] != -111) or (
                allcl['ex_bad2_name'] != -111 and allcl['ex_bad2_performance'] != -111) or \
                (allcl['ex_bad3_name'] != -111 and allcl['ex_bad3_performance'] != -111) or (
                allcl['ex_bad4_name'] != -111 and allcl['ex_bad4_performance'] != -111) or \
                (allcl['ex_bad5_name'] != -111 and allcl['ex_bad5_performance'] == -111) or (
                allcl['ex_bad6_name'] != -111 and allcl['ex_bad6_performance'] == -111) or \
                (allcl['ex_bad7_name'] != -111 and allcl['ex_bad7_performance'] == -111) or (
                allcl['ex_bad8_name'] != -111 and allcl['ex_bad8_performance'] == -111) or \
                (allcl['ex_bad9_name'] != -111 and allcl['ex_bad9_performance'] == -111) or (
                allcl['ex_bad_name_performance'] != -111 ):
            dict_stratege_child_br['BR0007'] = 100
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0007'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        print('sum', sum([allcl['als_m6_nsloan_count'], allcl['als_m6_cons_count'], allcl['als_m6_autofin_count'],
                          allcl['als_m6_sloan_count'], allcl['als_m6_finlea_count'], allcl['als_m6_else_count']]))
        if sum([allcl['als_m6_nsloan_count'], allcl['als_m6_cons_count'], allcl['als_m6_autofin_count'],
                allcl['als_m6_sloan_count'], allcl['als_m6_finlea_count'], allcl['als_m6_else_count']]) >= 5.0 or \
                sum([allcl['als_m12_nsloan_count'], allcl['als_m12_cons_count'], allcl['als_m12_autofin_count'],
                     allcl['als_m12_sloan_count'], allcl['als_m12_finlea_count'], allcl['als_m12_else_count']]) >= 6.0:
            dict_stratege_child_br['BR0008'] = 89
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0008'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['alm_d7_cell_nbank_else_allnum'] >= 2.0 or allcl['alm_d15_cell_nbank_allnum'] >= 5.0 or allcl[
            'als_m1_cell_nbank_else_allnum'] >= 6.0 or \
                allcl['alm_d7_id_nbank_else_allnum'] >= 2.0 or allcl['alm_d15_id_nbank_allnum'] >= 5.0 or allcl[
            'als_m1_id_nbank_else_allnum'] >= 6.0:
            dict_stratege_child_br['BR0009'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0009'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_pdl_allnum'] >= 4.0 or allcl['als_m3_cell_pdl_allnum'] >= 10.0 or allcl[
            'als_m1_id_pdl_allnum'] >= 4.0 or allcl['als_m3_id_pdl_allnum'] >= 10.0:
            dict_stratege_child_br['BR0010'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0010'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_rel_count'], allcl['als_m6_pdl_count'], allcl['als_m6_caon_count'],
                allcl['als_m6_caoff_count'], allcl['als_m6_coon_count'], allcl['als_m6_cooff_count'],
                allcl['als_m6_af_count'], allcl['als_m6_oth_count']]) >= 6.0 or \
                sum([allcl['als_m12_rel_count'], allcl['als_m12_pdl_count'], allcl['als_m12_caon_count'],
                     allcl['als_m12_caoff_count'], allcl['als_m12_coon_count'], allcl['als_m12_cooff_count'],
                     allcl['als_m12_af_count'], allcl['als_m12_oth_count']]) >= 7.0:
            dict_stratege_child_br['BR0011'] = 89
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0011'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_caon_allnum'] >= 2.0 or allcl['als_m1_id_caon_allnum'] >= 2.0:
            dict_stratege_child_br['BR0012'] = 62
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0012'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m1_caon_count'],
                allcl['als_m1_caoff_count'], allcl['als_m1_coon_count'], allcl['als_m1_cooff_count'],
                allcl['als_m1_af_count'], allcl['als_m1_oth_count']]) >= 4.0 or \
                sum([allcl['als_m3_rel_count'], allcl['als_m3_pdl_count'], allcl['als_m3_caon_count'],
                     allcl['als_m3_caoff_count'], allcl['als_m3_coon_count'], allcl['als_m3_cooff_count'],
                     allcl['als_m3_af_count'], allcl['als_m3_oth_count']]) >= 5.0:
            dict_stratege_child_br['BR0013'] = 89
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0013'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_nbank_allnum'] >= 29.0 or allcl['als_m12_cell_nbank_else_allnum'] >= 23.0 or allcl[
            'als_m12_id_nbank_allnum'] >= 29.0 or allcl['als_m12_id_nbank_else_allnum'] >= 23.0:
            dict_stratege_child_br['BR0014'] = 87
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0014'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_id_pdl_allnum'] >= 3.0 or allcl['als_m3_cell_pdl_allnum'] >= 7.0 or allcl[
            'als_m3_id_pdl_allnum'] >= 7.0:
            dict_stratege_child_br['BR0015'] = 76
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0015'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_oth_allnum'] >= 4.0 or allcl['als_m12_id_oth_allnum'] >= 4.0:
            dict_stratege_child_br['BR0016'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0016'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_pdl_allnum'] >= 17.0 or allcl['als_m12_id_pdl_allnum'] >= 17.0:
            dict_stratege_child_br['BR0017'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0017'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_nsloan_count'], allcl['als_m1_cons_count'], allcl['als_m1_autofin_count'],
                allcl['als_m1_sloan_count'], allcl['als_m1_finlea_count'], allcl['als_m1_else_count']]) >= 4.0:
            dict_stratege_child_br['BR0018'] = 89
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0018'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m6_cell_caon_allnum'] >= 6.0 or allcl['als_m6_id_caon_allnum'] >= 6.0 or allcl[
            'als_m12_cell_caon_allnum'] >= 8.0 or allcl['als_m12_id_caon_allnum'] >= 8.0:
            dict_stratege_child_br['BR0019'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0019'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_id_nbank_week_allnum'] >= 3.0 or allcl['als_m1_cell_nbank_week_allnum'] >= 3.0 or allcl[
            'als_m12_cell_nbank_week_allnum'] >= 8.0 or allcl['als_m12_id_nbank_week_allnum'] >= 8.0:
            dict_stratege_child_br['BR0020'] = 77
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0020'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_nbank_night_orgnum'] >= 3.0 or allcl['als_m12_id_nbank_night_orgnum'] >= 3.0:
            dict_stratege_child_br['BR0021'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0021'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_nsloan_count'], allcl['als_m1_cons_count'], allcl['als_m1_autofin_count'],
                allcl['als_m1_sloan_count'], allcl['als_m1_finlea_count'], allcl['als_m1_else_count']]) >= 3.0:
            dict_stratege_child_br['BR0022'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0022'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_nbank_allnum'] >= 21.0 or allcl['als_m12_id_nbank_allnum'] >= 21.0 or allcl[
            'als_m12_cell_nbank_else_allnum'] >= 15.0 or allcl['als_m12_id_nbank_else_allnum'] >= 15.0:
            dict_stratege_child_br['BR0023'] = 77
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0023'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_oth_allnum'] >= 3.0 or allcl['als_m12_cell_oth_allnum'] >= 3.0:
            dict_stratege_child_br['BR0024'] = 74
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0024'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_nbank_else_allnum'] >= 2.0 or allcl['als_m1_id_nbank_else_allnum'] >= 2.0:
            dict_stratege_child_br['BR0025'] = 63
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0025'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_pdl_allnum'] >= 12.0 or allcl['als_m12_id_pdl_allnum'] >= 12.0:
            dict_stratege_child_br['BR0026'] = 70
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0026'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_rel_count'], allcl['als_m6_pdl_count'], allcl['als_m6_caon_count'],
                allcl['als_m6_caoff_count'], allcl['als_m6_coon_count'], allcl['als_m6_cooff_count'],
                allcl['als_m6_af_count'], allcl['als_m6_oth_count']]) >= 5.0 or \
                sum([allcl['als_m12_rel_count'], allcl['als_m12_pdl_count'], allcl['als_m12_caon_count'],
                     allcl['als_m12_caoff_count'], allcl['als_m12_coon_count'], allcl['als_m12_cooff_count'],
                     allcl['als_m12_af_count'], allcl['als_m12_oth_count']]) >= 6.0:
            dict_stratege_child_br['BR0027'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0027'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_max_monnum'] >= 6.0 or allcl['als_m12_cell_max_monnum'] >= 6.0:
            dict_stratege_child_br['BR0028'] = 60
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0028'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m6_cell_caon_allnum'] >= 4.0 or allcl['als_m6_id_caon_allnum'] >= 4.0 or allcl[
            'als_m12_id_caon_allnum'] >= 5.0 or allcl['als_m12_cell_caon_allnum'] >= 5.0:
            dict_stratege_child_br['BR0029'] = 77
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0029'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_nbank_night_orgnum'] >= 2.0 or allcl['als_m12_cell_nbank_night_orgnum'] >= 2.0:
            dict_stratege_child_br['BR0030'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0030'] = 72
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_pdl_allnum'] >= 2.0 or allcl['als_m1_id_pdl_allnum'] >= 2.0 or allcl[
            'als_m3_id_pdl_allnum'] >= 4.0 or allcl['als_m3_cell_pdl_allnum'] >= 4.0:
            dict_stratege_child_br['BR0031'] = 64
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0031'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['sl_id_bad_info'] == 0.0 and allcl['sl_id_bad_info_time'] <= 2.0:
            dict_stratege_child_br['BR0032'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0032'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['ex_execut1_name'] != "" and allcl['ex_execut1_statute'] != "已结案") or (
                allcl['ex_execut2_name'] != "" and allcl['ex_execut2_statute'] != "已结案") or \
                (allcl['ex_execut3_name'] != "" and allcl['ex_execut3_statute'] != "已结案") or (
                allcl['ex_execut4_name'] != "" and allcl['ex_execut4_statute'] != "已结案") or \
                (allcl['ex_execut5_name'] != "" and allcl['ex_execut5_statute'] != "已结案") or (
                allcl['ex_execut6_name'] != "" and allcl['ex_execut6_statute'] != "已结案") or \
                (allcl['ex_execut7_name'] != "" and allcl['ex_execut7_statute'] != "已结案") or (
                allcl['ex_execut8_name'] != "" and allcl['ex_execut8_statute'] != "已结案") or \
                (allcl['ex_execut9_name'] != "" and allcl['ex_execut9_statute'] != "已结案") or (
                allcl['ex_execut10_name'] != "" and allcl['ex_execut10_statute'] != "已结案"):
            dict_stratege_child_br['BR0033'] = 80
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0033'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m1_caon_count'],
                allcl['als_m1_caoff_count'], allcl['als_m1_coon_count'], allcl['als_m1_cooff_count'],
                allcl['als_m1_af_count'], allcl['als_m1_oth_count']]) >= 3.0 or \
                sum([allcl['als_m3_rel_count'], allcl['als_m3_pdl_count'], allcl['als_m3_caon_count'],
                     allcl['als_m3_caoff_count'], allcl['als_m3_coon_count'], allcl['als_m3_cooff_count'],
                     allcl['als_m3_af_count'], allcl['als_m3_oth_count']]) >= 4.0:
            dict_stratege_child_br['BR0034'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0034'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['ir_m6_id_x_biz_addr_cnt'] >= 4.0 or allcl['ir_m6_id_x_home_addr_cnt'] >= 4.0 or allcl[
            'ir_m6_id_x_tel_home_cnt'] >= 4.0 or allcl['ir_m6_id_x_cell_cnt'] >= 3.0 or allcl['ir_m6_id_x_mail_cnt'] >= 4.0:
            dict_stratege_child_br['BR0035'] = 60
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0035'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_id_nbank_week_allnum'] >= 2.0 or allcl['als_m1_cell_nbank_week_allnum'] >= 2.0 or allcl[
            'als_m12_cell_nbank_week_allnum'] >= 5.0 or allcl['als_m12_id_nbank_week_allnum'] >= 5.0:
            dict_stratege_child_br['BR0036'] = 64
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0036'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_nbank_allnum'] >= 14.0 or allcl['als_m12_id_nbank_allnum'] >= 14.0 or allcl[
            'als_m12_cell_nbank_else_allnum'] >= 7.0 or allcl['als_m12_id_nbank_else_allnum'] >= 7.0:
            dict_stratege_child_br['BR0037'] = 62
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0037'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['ir_m12_id_x_home_addr_cnt'] >= 7.0 or allcl['ir_m12_id_x_tel_home_cnt'] >= 5.0 or allcl[
            'ir_m12_id_x_cell_cnt'] >= 4.0 or allcl['ir_m12_id_x_mail_cnt'] >= 5.0 or \
                allcl['ir_m3_id_x_tel_home_cnt'] >= 4.0 or allcl['ir_id_x_cell_cnt'] >= 5.0 or allcl[
            'ir_id_x_mail_cnt'] >= 5.0:
            dict_stratege_child_br['BR0038'] = 80
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0038'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_oth_allnum'] >= 2.0 or allcl['als_m12_cell_oth_allnum'] >= 2.0:
            dict_stratege_child_br['BR0039'] = 63
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0039'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_nsloan_count'], allcl['als_m6_cons_count'], allcl['als_m6_autofin_count'],
                allcl['als_m6_sloan_count'], allcl['als_m6_finlea_count'], allcl['als_m6_else_count']]) >= 4.0 or \
                allcl['als_m12_organization_typeall'] >= 5.0:
            dict_stratege_child_br['BR0040'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0040'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_pdl_allnum'] >= 7.0 or allcl['als_m12_id_pdl_allnum'] >= 7.0:
            dict_stratege_child_br['BR0041'] = 60
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0041'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_caon_allnum'] >= 3.0 or allcl['als_m12_cell_caon_allnum'] >= 3.0:
            dict_stratege_child_br['BR0042'] = 63
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0042'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['alm_d7_cell_nbank_else_allnum'] >= 1.0 or allcl['alm_d7_id_nbank_else_allnum'] >= 1.0 or allcl[
            'alm_d15_cell_nbank_allnum'] >= 3.0 or \
                allcl['alm_d15_id_nbank_allnum'] >= 3.0 or allcl['als_m1_cell_nbank_else_allnum'] >= 4.0 or allcl[
            'als_m1_id_nbank_else_allnum'] >= 4.0:
            dict_stratege_child_br['BR0043'] = 70
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0043'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_d15_cell_cooff_allnum'] >= 1.0 or allcl['als_d15_id_cooff_allnum'] >= 1.0 or allcl[
            'als_m12_id_cooff_orgnum'] >= 3.0 or allcl['als_m12_cell_cooff_orgnum'] >= 3.0:
            dict_stratege_child_br['BR0044'] = 91
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0044'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_rel_count'], allcl['als_m6_pdl_count'], allcl['als_m6_caon_count'],
                allcl['als_m6_caoff_count'], allcl['als_m6_coon_count'], allcl['als_m6_cooff_count'],
                allcl['als_m6_af_count'], allcl['als_m6_oth_count']]) >= 4.0 or \
                sum([allcl['als_m12_rel_count'], allcl['als_m12_pdl_count'], allcl['als_m12_caon_count'],
                     allcl['als_m12_caoff_count'], allcl['als_m12_coon_count'], allcl['als_m12_cooff_count'],
                     allcl['als_m12_af_count'], allcl['als_m12_oth_count']]) >= 5.0:
            dict_stratege_child_br['BR0045'] = 57
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0045'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_nsloan_count'], allcl['als_m1_cons_count'], allcl['als_m1_autofin_count'],
                allcl['als_m1_sloan_count'], allcl['als_m1_finlea_count'], allcl['als_m1_else_count']]) >= 2.0:
            dict_stratege_child_br['BR0046'] = 57
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0046'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_id_caon_allnum'] >= 1.0 or allcl['als_m1_cell_caon_allnum'] >= 1.0:
            dict_stratege_child_br['BR0047'] = 41
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0047'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_cooff_orgnum'] >= 2.0 or allcl['als_m12_id_cooff_orgnum'] >= 2.0:
            dict_stratege_child_br['BR0048'] = 68
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0048'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m1_caon_count'],
                allcl['als_m1_caoff_count'], allcl['als_m1_coon_count'], allcl['als_m1_cooff_count'],
                allcl['als_m1_af_count'], allcl['als_m1_oth_count']]) >= 2.0 or \
                sum([allcl['als_m3_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m3_caon_count'],
                     allcl['als_m3_caoff_count'], allcl['als_m3_coon_count'], allcl['als_m3_cooff_count'],
                     allcl['als_m3_af_count'], allcl['als_m3_oth_count']]) >= 3.0:
            dict_stratege_child_br['BR0049'] = 57
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0049'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_nsloan_count'], allcl['als_m6_cons_count'], allcl['als_m6_autofin_count'],
                allcl['als_m6_sloan_count'], allcl['als_m6_finlea_count'], allcl['als_m6_else_count']]) >= 3.0 or \
                sum([allcl['als_m12_nsloan_count'], allcl['als_m12_cons_count'], allcl['als_m2_autofin_count'],
                     allcl['als_m12_sloan_count'], allcl['als_m12_finlea_count'], allcl['als_m12_else_count']]) >= 4.0:
            dict_stratege_child_br['BR0050'] = 57
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0050'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_cell_nbank_else_allnum'] >= 1.0 or allcl['als_m1_id_nbank_else_allnum'] >= 1.0:
            dict_stratege_child_br['BR0051'] = 46
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0051'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_oth_allnum'] >= 1.0 or allcl['als_m12_cell_oth_allnum'] >= 1.0:
            dict_stratege_child_br['BR0052'] = 48
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0052'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_rel_count'], allcl['als_m6_pdl_count'], allcl['als_m6_caon_count'],
                allcl['als_m6_caoff_count'], allcl['als_m6_coon_count'], allcl['als_m6_cooff_count'],
                allcl['als_m6_af_count'], allcl['als_m6_oth_count']]) >= 3.0 or \
                sum([allcl['als_m12_rel_count'], allcl['als_m12_pdl_count'], allcl['als_m12_caon_count'],
                     allcl['als_m12_caoff_count'], allcl['als_m12_coon_count'], allcl['als_m12_cooff_count'],
                     allcl['als_m12_af_count'], allcl['als_m6_oth_count']]) >= 4.0:

            dict_stratege_child_br['BR0053'] = 43
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0053'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_pdl_allnum'] >= 3.0 or allcl['als_m12_id_pdl_allnum'] >= 3.0:
            dict_stratege_child_br['BR0054'] = 44
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0054'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['ald_cell_nbank_allnum'] >= 5.0 or allcl['ald_id_nbank_allnum'] >= 5.0:
            dict_stratege_child_br['BR0055'] = 85
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0055'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_nbank_night_orgnum'] >= 1.0 or allcl['als_m12_cell_nbank_night_orgnum'] >= 1.0:
            dict_stratege_child_br['BR0056'] = 52
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0056'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m1_id_nbank_week_allnum'] >= 1.0 or allcl['als_m1_cell_nbank_week_allnum'] >= 1.0 or allcl[
            'als_m12_cell_nbank_week_allnum'] >= 2.0 or allcl['als_m12_id_nbank_week_allnum'] >= 2.0:
            dict_stratege_child_br['BR0057'] = 43
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0057'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m3_id_pdl_allnum'] >= 1.0 or allcl['als_m3_cell_pdl_allnum'] >= 1.0:
            dict_stratege_child_br['BR0058'] = 42
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0058'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m6_nsloan_count'], allcl['als_m6_cons_count'], allcl['als_m6_autofin_count'],
                allcl['als_m6_sloan_count'], allcl['als_m6_finlea_count'], allcl['als_m6_else_count']]) >= 2.0 or \
                sum([allcl['als_m12_nsloan_count'], allcl['als_m12_cons_count'], allcl['als_m12_autofin_count'],
                     allcl['als_m12_sloan_count'], allcl['als_m12_finlea_count'], allcl['als_m12_else_count']]) >= 3.0:
            dict_stratege_child_br['BR0059'] = 43
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0059'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_nsloan_count'], allcl['als_m1_cons_count'], allcl['als_m1_autofin_count'],
                allcl['als_m1_sloan_count'], allcl['als_m1_finlea_count'], allcl['als_m1_else_count']]) >= 1.0:
            dict_stratege_child_br['BR0060'] = 43
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0060'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_cell_nbank_allnum'] >= 3.0 or allcl['als_m12_id_nbank_allnum'] >= 3.0 or allcl[
            'als_m12_cell_nbank_else_allnum'] >= 2.0 or allcl['als_m12_id_nbank_else_allnum'] >= 2.0:
            dict_stratege_child_br['BR0061'] = 47
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0061'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['als_m12_id_max_monnum'] >= 2.0 or allcl['als_m12_cell_max_monnum'] >= 2.0:
            dict_stratege_child_br['BR0062'] = 42
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0062'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if sum([allcl['als_m1_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m1_caon_count'],
                allcl['als_m1_caoff_count'], allcl['als_m1_coon_count'], allcl['als_m1_cooff_count'],
                allcl['als_m1_af_count'], allcl['als_m1_oth_count']]) >= 1.0 or \
                sum([allcl['als_m3_rel_count'], allcl['als_m1_pdl_count'], allcl['als_m3_caon_count'],
                     allcl['als_m3_caoff_count'], allcl['als_m3_coon_count'], allcl['als_m3_cooff_count'],
                     allcl['als_m3_af_count'], allcl['als_m3_oth_count']]) >= 2.0:
            dict_stratege_child_br['BR0063'] = 43
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0063'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['sl_id_bank_bad'] == 0.0 and allcl['sl_id_bank_bad_time'] <= 2.0) or (
                allcl['sl_cell_bank_bad'] == 0.0 and allcl['sl_cell_bank_bad_time'] <= 2.0):
            dict_stratege_child_br['BR0064'] = 80
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0064'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['sl_id_bad_info'] == 0.0 and allcl['sl_id_bad_info_time'] >= 3.0:
            dict_stratege_child_br['BR0065'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0065'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['sl_id_bank_fraud'] == 0.0 and allcl['sl_id_bank_fraud_time'] <= 2.0) or (
                allcl['sl_cell_bank_fraud'] == 0.0 and allcl['sl_cell_bank_fraud_time'] <= 2.0):
            dict_stratege_child_br['BR0066'] = 50
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0066'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['sl_id_bank_overdue'] == 0.0 and allcl['sl_id_bank_overdue_time'] <= 2.0) or (
                allcl['sl_cell_bank_overdue'] == 0.0 and allcl['sl_cell_bank_overdue_time'] <= 2.0):
            dict_stratege_child_br['BR0067'] = 30
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0067'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if allcl['sl_id_court_executed'] == 0.0 and allcl['sl_id_court_executed_time'] >= 3.0:
            dict_stratege_child_br['BR0068'] = 70
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0068'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        if (allcl['sl_id_bank_bad'] == 0.0 and allcl['sl_id_bank_bad_time'] >= 3.0) or (
                allcl['sl_cell_bank_bad'] == 0.0 and allcl['sl_cell_bank_bad_time'] >= 3.0):
            dict_stratege_child_br['BR0069'] = 75
            dict_strategy_group_br.update(dict_stratege_child_br)
        else:
            dict_stratege_child_br['BR0069'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
            # if  :
            #    dict_stratege_child_br['BR0070'] = 60
            #    dict_strategy_group_br.update(dict_stratege_child_br)
            # else:
            dict_stratege_child_br['BR0070'] = 0
            dict_strategy_group_br.update(dict_stratege_child_br)
        ###找不到键
        # if  allcl['sl_id_court_bad'] == 0.0  and  allcl['sl_id_court_bad_time'] <= 2.0  :
        #     dict_stratege_child_br['BR0071'] = 100
        #     dict_strategy_group_br.update(dict_stratege_child_br)
        # else:
        #     dict_stratege_child_br['BR0071'] = 0
        #     dict_strategy_group_br.update(dict_stratege_child_br)
        return dict_strategy_group, dict_strategy_group_br
