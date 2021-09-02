from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm,DynamicLoginForm

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        login_form=DynamicLoginForm()
        return render(request,'login.html',{'login_form':login_form})

    def post(self,request):
        # username=request.POST.get('username','')
        # password=request.POST.get('password','')

        # if not username:
        #     return render(request,'login.html',{'msg':'请输入用户名'})
        # elif not password:
        #     return render(request,'login.html',{'msg':'请输入密码'})

        # 表单验证
        login_form=LoginForm(request.POST)
        if login_form.is_valid():

            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']

            # 通过用户名和密码判断用户名是否存在
            user=authenticate(username=username,password=password)
            if user is not None:
                # 查询到用户
                login(request,user)
                # 登录成功之后应该怎么返回页面
                return HttpResponseRedirect(reverse('index'))
            else:
                # 未查询到用户
                return render(request,'login.html',{'msg':'用户名或密码错误','login_form': login_form})

        else:
            return render(request, 'login.html', {'login_form': login_form})