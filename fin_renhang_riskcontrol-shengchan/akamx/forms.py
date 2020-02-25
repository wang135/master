from django import forms
#from .models import OperatingConditions, Compangyinfo,IncreasingLetters,Peopleinfo,Zichanfuzhai,Socialrelations
from .models import Peopleinfo,jsonss
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers


# class AddForm(ModelForm):
#     class Meta:
#         model = Peopleinfo
#         fields = '__all__'
#         exclude = ['dateTime']

class PeopleinfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peopleinfo
        fields = "__all__"
       # exclude = ['dateTime']
class jsonssModelSerializer(serializers.ModelSerializer):
    #user = serializers.JSONField()
    code = serializers.JSONField()
    dict_credit_group = serializers.JSONField()
    bl_json = serializers.JSONField()
    cl_td = serializers.JSONField()
    cl_br = serializers.JSONField()
    df1_dict = serializers.JSONField()
    score = serializers.JSONField()
    class Meta:
        model = jsonss
        fields = "__all__"
        #exclude = ('user',)
