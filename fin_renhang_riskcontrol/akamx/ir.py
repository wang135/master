import numpy as np
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')


class Score:
    def __init__(self):
        self.col = ["woe_als_m12_id_nbank_orgnum", "woe_cell_city_ec_level", "woe_i_max_cnt_partner_daily_Loan_finance_365day", "woe_i_get_node_rank_value_Loan_all_all",
                    "woe_融资金额", 'woe_age_frg', "woe_ir_m6_cell_x_linkman_cell_cnt",
                    "woe_sl_gender", "woe_cell_province", 'woe_cell_city', "flagy"]

    theProv1 = {'上海', '江西', '湖北', '河北', 'M_B'}
    theProv2 = {'广东', '湖南', '重庆', '浙江', '内蒙古', '河南', '山东', '天津', '黑龙江'}
    theProv3 = {'贵州', '青海', '陕西', '山西', '四川', '辽宁', '福建', '新疆', '广西', '江苏', '西藏'}
    theProv4 = {'云南', '甘肃', '安徽', '海南', '宁夏', '北京', '吉林'}

    theCity1 = {'莆田', '衡水', '烟台', '吉安', '承德', '秦皇岛', '南充', '永州', '宁波', '龙岩', '开封',
                '万州', '邵阳', '邯郸', '赤峰', '奎屯', '临沂', '淮安', '威海', '三门峡', 'M_B', '乌海', '湘潭', '赣州',
                '玉树', '大庆', '连云港', '韶关', '清远', '九江', '咸宁', '江门', '日照', '衢州', '安阳', '泰州', '甘孜',
                '抚顺', '揭阳', '钦州', '松原', '通化', '贺州', '阿坝'}

    theCity2 = {'潍坊', '深圳', '东莞', '乐山', '南宁', '武汉', '盘锦', '临汾', '成都', '兴义', '岳阳', '廊坊',
                '惠州', '常德', '崇左', '厦门', '荆州', '包头', '沧州', '青岛', '柳州', '大连', '苏州', '海西', '南通', '襄阳',
                '桂林', '广安', '邢台', '驻马店', '台州', '绍兴', '渭南', '金华', '德州', '娄底', '阿拉善盟', '湘西', '眉山',
                '鸡西', '枣庄', '无锡', '凯里', '保定', '海南', '武威', '亳州', '白城', '莱芜', '泰安', '盐城', '吐鲁番', '营口',
                '汕尾', '海北', '茂名', '阳江', '博乐', '仙桃', '克拉玛依', '海拉尔', '云浮', '珲春', '鹰潭', '黑河', '西昌', '延边'}

    theCity3 = {'重庆', '宝鸡', '丽水', '北京', '昆明', '萍乡', '宜宾', '平凉', '天津', '曲靖', '漳州', '西安', '遵义',
                '泸州', '太原', '铜仁', '定西', '忻州', '锡林浩特', '巴中', '石家庄', '延安', '嘉兴', '恩施', '广元', '达州', '白银',
                '银川', '海口', '许昌', '庆阳', '酒泉', '内江', '西双版纳', '吉首', '广州', '凉山', '吕梁', '西宁', '长治', '陇南',
                '天水', '玉溪', '株洲', '淮南', '济南', '大同', '洛阳', '汕头', '温州', '文山', '南京', '济宁', '珠海', '南阳', '果洛',
                '张掖', '咸阳', '格尔木', '唐山', '晋城', '大理', '红河', '阜阳', '海东', '保山', '宜昌', '镇江', '贵阳', '楚雄', '固原',
                '合肥', '绵阳', '泉州', '巴彦淖尔', '贵港', '菏泽', '佛山', '杭州', '兰州', '郑州', '上海', '上饶', '阿克苏', '益阳', '石河子',
                '嘉峪关', '汉中', '景德镇', '运城', '郴州', '毕节', '涪陵', '芜湖', '丽江', '玉林', '六安', '乌鲁木齐', '安顺', '临沧', '聊城',
                '扬州', '中卫', '六盘水', '福州', '长沙', '葫芦岛', '三明', '共和', '怀化', '黔江', '信阳', '淄博', '迪庆', '晋中', '中山',
                '吴忠', '乌兰察布', '沈阳', '昭通', '张家口', '都匀', '徐州', '新乡', '金昌', '黄南', '通辽', '思茅', '黔东南', '黄冈', '德阳',
                '随州', '德令哈', '南昌', '伊犁', '安庆', '衡阳', '百色', '舟山', '鄂尔多斯', '抚州', '资阳', '常州', '河池', '海晏', '濮阳', '朔州',
                '黔西南', '攀枝花', '淮北', '四平', '肇庆', '宜春', '滨州', '周口', '甘南', '铁岭', '安康', '焦作', '梅州', '平顶山', '黔南',
                '池州', '呼和浩特', '自贡', '朝阳', '滁州', '本溪', '怒江', '宁德', '哈尔滨', '荆门', '牡丹江', '临夏', '石嘴山', '雅安', '鞍山',
                '那曲', '辽阳', '白山', '昌吉', '湛江', '梧州', '商丘', '孝感', '哈密', '克孜勒苏', '德宏', '东营', '榆林', '防城港', '宿迁', '乌兰浩特',
                '长春', '锦州', '湖州', '蚌埠', '北海', '十堰', '江汉', '宿州', '集宁', '林芝', '大兴安岭', '吉林', '宣城', '漯河', '商洛', '遂宁', '丹东',
                '普洱', '张家界', '河源', '铜川', '喀什', '阿勒泰', '阜新', '南平', '伊春', '拉萨', '阳泉', '阿里', '锡林郭勒盟', '潮州', '鄂州', '新余',
                '来宾', '铜陵', '库尔勒', '黄石'}

    @staticmethod
    def WOE_als(df: pd.DataFrame) -> float:
        temp = df['als_m12_id_nbank_orgnum']
        if temp <= -99:
            return -0.9905
        elif temp <= -1:
            return -0.6534
        elif temp <= 1:
            return -0.2642
        elif temp <= 2:
            return 0.0430
        elif temp <= 5:
            return 0.4120
        elif temp <= 10:
            return 1.1025
        else:
            return 1.3919

    @staticmethod
    def WOE_city_ec(df: pd.DataFrame) -> float:
        temp = df['cell_city_ec_level']
        if temp <= -1:
            return -0.1563
        elif temp <= 1200:
            return -0.4482
        elif temp <= 1350:
            return -0.3093
        elif temp <= 1900:
            return 0.0475
        elif temp <= 3000:
            return 0.0622
        else:
            return 0.6009

    @staticmethod
    def WOE_i_max_cnt_partner_daily_Loan_finance_365day(df: pd.DataFrame) -> float:
        temp = df['i_max_cnt_partner_daily_Loan_finance_365day']
        if temp <= -99:
            return -1.0218
        elif temp <= 1:
            return -0.3546
        elif temp <= 2:
            return 0.5453
        else:
            return 1.1982

    @staticmethod
    def WOE_i_get_node_rank_value_Loan_all_all(df: pd.DataFrame) -> float:
        temp = df['i_get_node_rank_value_Loan_all_all']
        if temp <= -1111:
            return -0.1196
        elif temp <= -999:
            return -0.3269
        elif temp == 0:
            return 0.5136
        else:
            return 0.5265

    @staticmethod
    def WOE_RZJE(df: pd.DataFrame) -> float:
        temp = df['融资金额']
        if temp <= 70000:
            return 0.0199
        elif temp <= 80000:
            return -0.4453
        elif temp <= 95000:
            return -0.3649
        elif temp <= 110000:
            return 0.2451
        else:
            return 0.5391

    @staticmethod
    def WOE_age_frg(df: pd.DataFrame) -> float:
        if df['frg_list_level'] <= -99 and df['apply_age'] < 25:
            return -0.2532
        elif df['frg_list_level'] <= -99 and df['apply_age'] < 45:
            return -0.5545
        elif df['frg_list_level'] <= -99 and df['apply_age'] >= 45:
            return -0.4625
        elif df['frg_list_level'] < 5:
            return 0.7118
        else:
            return 1.2803

    @staticmethod
    def WOE_ir(df: pd.DataFrame) -> float:
        temp = df['ir_m6_cell_x_linkman_cell_cnt']
        if temp <= -99:
            return -1.1601
        elif temp <= -1:
            return -0.5295
        else:
            return 0.4640

    @staticmethod
    def WOE_SS(df: pd.DataFrame) -> float:
        theSp = df['flag_specialList_c']
        thegen = df['gender']
        if thegen == 0 and theSp == 0:
            return -0.1126
        elif thegen == 1 and theSp == 0:
            return -0.0585
        else:
            return 0.8694

    @staticmethod
    def WOE_cell_province(df: pd.DataFrame) -> float:
        temp = df['cell_province']
        if temp in Score.theProv1:
            return 0.5578
        elif temp in Score.theProv2:
            return 0.4508
        elif temp in Score.theProv3:
            return 0.0003
        else:
            return -0.4442

    @staticmethod
    def WOE_cell_city(df: pd.DataFrame) -> float:
        temp = df['cell_city']
        if temp in Score.theCity1:
            return 0.7762
        elif temp in Score.theCity2:
            return 0.5512
        else:
            return -0.1598

    @staticmethod
    def get_odds(df: pd.DataFrame) -> pd.DataFrame:
        df["odds"] = df["woe_als_m12_id_nbank_orgnum"] * 0.38929019234372647 \
                     + df["woe_cell_city_ec_level"] * 0.4256609883834146 \
                     + df["woe_i_max_cnt_partner_daily_Loan_finance_365day"] * 0.3376071667460782 \
                     + df["woe_i_get_node_rank_value_Loan_all_all"] * 0.2793197568224026 \
                     + df["woe_融资金额"] * 0.8403668316875686 \
                     + df["woe_age_frg"] * 0.2150064685794368 \
                     + df["woe_ir_m6_cell_x_linkman_cell_cnt"] * 0.2794698572885128 \
                     + df["woe_sl_gender"] * 0.49792835781599715 \
                     + df["woe_cell_province"] * 0.5784174302105042 \
                     + df["woe_cell_city"] * 0.5417858499432695 \
                     - 2.9770612620547205
        return df

    @staticmethod
    def get_score(odds: pd.Series) -> pd.Series:
        p_1 = 1 / (1 + np.exp(-odds))
        score = 655 - 95 * np.log2((p_1 / (1 - p_1)) / (0.05 / 0.95))
        return score

    def derive(self, df: pd.DataFrame) -> pd.DataFrame:
        df["woe_als_m12_id_nbank_orgnum"] = df.apply(Score.WOE_als, axis=1)
        df["woe_cell_city_ec_level"] = df.apply(Score.WOE_city_ec, axis=1)
        df["woe_i_max_cnt_partner_daily_Loan_finance_365day"] = df.apply(Score.WOE_i_max_cnt_partner_daily_Loan_finance_365day, axis=1)
        df["woe_i_get_node_rank_value_Loan_all_all"] = df.apply(Score.WOE_i_get_node_rank_value_Loan_all_all, axis=1)
        df["woe_融资金额"] = df.apply(Score.WOE_RZJE, axis=1)
        df["woe_age_frg"] = df.apply(Score.WOE_age_frg, axis=1)
        df["woe_ir_m6_cell_x_linkman_cell_cnt"] = df.apply(Score.WOE_ir, axis=1)
        df["woe_sl_gender"] = df.apply(Score.WOE_SS, axis=1)
        df["woe_cell_province"] = df.apply(Score.WOE_cell_province, axis=1)
        df["woe_cell_city"] = df.apply(Score.WOE_cell_city, axis=1)
        return df

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.derive(df)
        df = self.get_odds(df)
        df.loc[:, "score"] = df["odds"].apply(self.get_score)
        df.loc[(df["score"] < 300), "score"] = 300
        df.loc[(df["score"] > 1000), "score"] = 1000
        return df
