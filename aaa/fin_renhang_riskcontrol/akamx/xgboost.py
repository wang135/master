
import numpy as np
import pandas as pd
from akamx.lujing import lujings
# lujins = lujings()
# www = lujins.shenfen()
# print('wwwwwwwwwwwwwwww',www)
# xgb = lujins.xgb()
# feature = lujins.feature()
# id_yinshe = lujins.id_yinshe()
#
#
# cell_province =lujins.cell_province()
# cell_province['cell_province'] = cell_province['cell_province'].str.strip()
#
# cell_city = lujins.cell_city()[['cell_city','ids']]
# cell_city['cell_city'] = cell_city['cell_city'].str.strip()

class xgboost:
    # lujins = lujings()
    # www = lujins.shenfen()
    # xgb = lujins.xgb()
    # feature = lujins.feature()
    # id_yinshe = lujins.id_yinshe()
    #
    # cell_province = lujins.cell_province()
    # cell_province['cell_province'] = cell_province['cell_province'].str.strip()
    #
    # cell_city = lujins.cell_city()[['cell_city', 'ids']]
    # cell_city['cell_city'] = cell_city['cell_city'].str.strip()
    def __init__(self,data,dicts,dict_sex):
        self.data = data
        self.cellphone = dicts
        self.dict_sex = dict_sex
    def join(self):
        cell_province = lujings().cell_province()
        cell_province['cell_province'] = cell_province['cell_province'].str.strip()
        province = list(self.cellphone['cell_province'])[0]
        #print('111111', province)
        cell_city = lujings().cell_city()[['cell_city', 'ids']]
        cell_city['cell_city'] = cell_city['cell_city'].str.strip()
        city = list(self.cellphone['cell_city'])[0]
        #print('222222', city)

        self.data['cell_province'] = list(cell_province[cell_province['cell_province'] == province]['ids'])[0]
        #print('333333333333333333', cell_province[cell_province['cell_province'] == province]['ids'])
        # #print('qqqqqq',results_dicts)
        self.data['cell_city'] = list((cell_city[cell_city['cell_city'] == city]['ids']))[0]
        self.data.update(self.dict_sex)
        #print('dddddddddddddddddddddddd', self.data)
        return self.data
    def id_shenfen(self,id_no):
        id_yinshe = lujings().id_yinshe()
        id_city = lujings().id_city()

        ids = id_no[0:4]
        city = list(id_yinshe[id_yinshe['ID_4_digit'] == int(ids)]['City'])[0]
        ##print(city)
        idss = list(id_city[id_city['id_city'] == city]['ids'])[0]
        return idss
    def datas(self,results_dicts):
        ###xgb的输出
        # results_dicts['id_city'] = 'M_B'
        #results_dicts = self.join()
        df_all = pd.DataFrame([results_dicts], dtype='float')
        #print('pppppppppppppppp',df_all)

        df_all['frg_group_num'] = df_all['frg_group_num'].apply(lambda x: 1 if x == 'a' else (2 if x == 'b' else (3 if x == 'c' else (4 if x == 'd' else 4   ))))
        #print('qqqqqqqqqqq',df_all['frg_group_num'])
        #df_all['id_city'] = 1
        df_all['ir_id_x_cell_notmat_days'] = 0
        df_all['a86'] = -999
        df_all['b14'] = -999
        df_all['b2'] = -999
        df_all['b26'] = -999
        df_all['d40'] = -999
        df_all['b20'] = -999
        df_all['d15'] = -999

        # xgb = lujins.xgb()
        # feature = lujins.feature()
        #print('wwwwwwwwwwwwwwwwwwwwwww',list(df_all.columns))
        feature = lujings().feature()
        td_in = [x for x in feature if x not in list(df_all.columns)]
        #print('ttttttttttttttttttttttttttttttttttttttttttt', td_in)
        for ff in td_in:
            df_all[ff] = -99
        #print('eeeeeeeeeeeeeeee', df_all[feature])
        xgb = lujings().xgb()
        p = xgb.predict_proba(df_all[feature])[:, 1]
        s = (0.1 / 0.9) / (0.05 / 0.95)
        p_1 = 1 / (1 + s * np.exp(-np.log(p / (1 - p))))
        score = 652 - 95 * np.log((p_1 / (1 - p_1)) / (0.05 / 0.95))
        if score < 300:
            score = 300
        elif score > 1000:
            score = 1000
        else:
            score = score

        return score



