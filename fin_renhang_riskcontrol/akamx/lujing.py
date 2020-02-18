import os
from pickle import load

class lujings:
    def __init__(self,curname = os.path.dirname(os.path.abspath(__file__))):
        self.cur_dir= curname
    def shenfen(self):
        self.model_path = os.path.join(self.cur_dir, "pick/shenfen.pickle")
        self.shenfen = load(open(self.model_path, "rb"))

        return self.shenfen
