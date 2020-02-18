from django.db import models

# Create your models here.
class Peopleinfo(models.Model):
    #id = models.IntegerField()
    full_name = models.CharField(max_length=100,null=False,verbose_name='客户姓名') # 实际控制人信息
    id_no = models.CharField(max_length=100,null=False,verbose_name='身份证号')# 身份证号码
    cellphone = models.CharField(max_length=100,null=False,verbose_name='身份证号')# 电话
    dateTime = models.DateTimeField(auto_now_add=True) ###时间


class jsonss(models.Model):
    #user= models.OneToOneField(Peopleinfo, on_delete=models.CASCADE)
    #user = models.ForeignKey(to="Peopleinfo")
    full_name = models.CharField(max_length=100, null=False, verbose_name='客户姓名')  # 实际控制人信息
    id_no = models.CharField(max_length=100, null=False, verbose_name='身份证号')  # 身份证号码
    code = models.CharField(blank=True,max_length=100, null=True)
    dict_credit_group = models.TextField(blank=True,null=True)
    bl_json = models.CharField(blank=True,max_length=500, null=True)
    cl_td = models.TextField(blank=True,null=True)
    cl_br = models.TextField(blank=True, null=True)
    df1_dict= models.TextField(blank=True, max_length=500,null=True)
    score = models.CharField(blank=True,max_length=500, null=True)