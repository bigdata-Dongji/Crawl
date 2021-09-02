# encoding:utf8
'''
Creation time: 2020/11/30 21:24 
Update time:
Purpose:
'''
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username=forms.CharField(required=True,min_length=2)
    password=forms.CharField(required=True,min_length=3)



class DynamicLoginForm(forms.Form):
    # myfield = AnyOtherField()
    captcha = CaptchaField()