"""Gonghangguize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from ghrule import views as views
from akamx import views as view

urlpatterns = [
  #  url('admin/', admin.site.urls),
    url(r'^gonghang/$',views.gonghangrule.as_view()),
    url(r'^yunwei/$',views.yunwei.as_view()),
     url(r'^api/$',view.akmoxing.as_view()),
     url(r'^yun/$',view.yunwei.as_view()),

]