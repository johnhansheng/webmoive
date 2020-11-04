#!/usr/bin/env python 
# coding:utf-8

from django.urls import path
from . import views

app_name='users'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),

]

def signup(request):
    username=form.cleaned_data.get('username')
    raw_password1=form.cleaned_data.get('password1')
    user=authenticate(username=username,password=raw_password1)
    auth_login(request,user)