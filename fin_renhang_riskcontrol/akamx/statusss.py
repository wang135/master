

class Status:
    def __init__(self,lr_score,br_score,td_score,dict_credit_group,capital_code):
        self.lr_score = lr_score
        self.br_score = br_score
        self.td_score = td_score
        self.dict_credit_group =  dict_credit_group
        self.capital_code =capital_code
    def status(self):
        status = ''
        if self.capital_code== 'MSFL_ONLINE':
            if self.lr_score> 500 and self.dict_credit_group < 100 \
                    and self.td_score < 80 and self.br_score < 80:
                status = 1000

            else:
                status = 3000
        else:
            if self.lr_score > 615 and self.dict_credit_group < 100 \
                    and self.td_score < 80 and self.br_score < 80:
                status = 1000
            elif self.lr_score > 405 or self.dict_credit_group == 100 \
                    or self.td_score > 80 or self.br_score > 80:
                status = 3000
            else:
                status = 2000
        statuss = {'codes': status}
        return status