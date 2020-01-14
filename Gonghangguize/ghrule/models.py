from django.db import models



# Create your models here.
class Peopleinfogonghang(models.Model):
    #id = models.IntegerField()
    full_name = models.CharField(max_length=100,null=False,verbose_name='客户姓名') # 实际控制人信息
    id_no = models.CharField(max_length=100,null=False,verbose_name='身份证号')# 身份证号码
    #cellphone = models.CharField(max_length=100,null=False,verbose_name='电话号码')# 电话
    dateTime = models.DateTimeField(auto_now_add=True) ###时间