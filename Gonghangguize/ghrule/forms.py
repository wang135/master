from .models import Peopleinfogonghang
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers



class PeopleinfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peopleinfogonghang
        fields = "__all__"