'''
Created on 2018. 10. 6.

@author: user
'''
from django.urls import path
from .views import *
from blog.views import PostRegister
app_name = 'blog'
urlpatterns = [
    #뷰 클래스를 url 등록할 때, 뷰클래스명.as_view()로 등록함
    path('', Index.as_view(), name='index' ),
    #DetailView는 특정 객체를 찾기위해 pk(id 변수) 또는 slug 변수를 사용함
    #모델클래스의 기본키로 설정되있는 변수의 이름으로 URL 값을 넘겨줌
    path('<int:pk>/',Detail.as_view(), name='detail'),
    path('postR/',PostRegister.as_view(), name='registerP'),
    path('search/',searchP, name='search')
    ]








