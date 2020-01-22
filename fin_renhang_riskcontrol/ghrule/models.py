from django.db import models



# Create your models here.
class Peopleinfogonghang(models.Model):
    #id = models.IntegerField()
    full_name = models.CharField(max_length=100,null=False,verbose_name='客户姓名') # 实际控制人信息
    id_no = models.CharField(max_length=100,null=False,verbose_name='身份证号')# 身份证号码
    #cellphone = models.CharField(max_length=100,null=False,verbose_name='电话号码')# 电话
    dateTime = models.DateTimeField(auto_now_add=True) ###时间


class Rule(models.Model):
    full_name = models.CharField(max_length=100, null=False, verbose_name='客户姓名')  # 实际控制人信息
    id_no = models.CharField(max_length=100, null=False, verbose_name='身份证号')  # 身份证号码
    all_list_san = models.CharField(max_length=100,null=True,verbose_name='累计次数') # 逾期累计次数
    list_len_all= models.CharField(max_length=100,null=True,verbose_name='连续次数') # 连续次数
    cumulativeCompenAmount= models.CharField(max_length=100,null=True,verbose_name='保证人代偿') # 保证人代偿
    condit = models.CharField(max_length=100,null=True,verbose_name='状态') # 状态


