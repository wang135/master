from .models import Peopleinfogonghang,Rule
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule

        exclude = ('condit',)


class PeopleinfoModelSerializer(serializers.ModelSerializer):
    #rule_name = serializers.CharField(source='rule.full_name')
    #rule = serializers.PrimaryKeyRelatedField(label='rule_id',read_only=True)
    class Meta:
        #rule = serializers.PrimaryKeyRelatedField(read_only=True)
        model = Peopleinfogonghang
        fields = "__all__"
        #exclude = ('rule',)