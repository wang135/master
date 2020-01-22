from .models import Peopleinfogonghang,Rule
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers



class PeopleinfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peopleinfogonghang
        fields = "__all__"



class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule

        exclude = ('condit',)
