'''
Created on 2018. 9. 30.

@author: user
'''
from django.forms import ModelForm
#django에서 회원을 관리하는 모델클래스
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput
#회원가입에 사용할 폼
class SignupForm(ModelForm):
    def __init__(self,*args,**kwarg):
        super().__init__(*args,**kwarg)
        self.fields['password_check'].label = "비밀번호 확인"
        
    password_check =forms.CharField(max_length=200,
                                    widget=forms.PasswordInput()) 

    class Meta:
        model = User
        widgets={
            'password' : forms.PasswordInput()
            }
        fields = ['username','password','first_name',
                  'last_name','email']
        #fields or exclude
    #field_order : 입력양식 순서 지정(리스트형태)
    field_order = ['username','password','password_check',
                    'first_name','last_name','email']
#로그인에 사용할 폼
class LoginForm(ModelForm):
    class Meta:
        model = User
        #password 입력공간에 PasswordInput위젯 적용하기
        widgets={
            'password' : PasswordInput()
            }
        fields = ['username','password']









