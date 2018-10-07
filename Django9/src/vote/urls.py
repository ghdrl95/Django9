'''
Created on 2018. 9. 16.

@author: user
'''
from django.urls import path
from .views import *
from vote.views import questionUpdate, questionDelete, choiceDelete,\
    choiceRegister, choiceUpdate
#하위 urls 파일을 만들 경우, app_name변수가 필요함
#app_name : 해당 url들을 그룹핑하는 변수
app_name = 'vote' #장고 2.0이상인 경우 

urlpatterns = [
    #http://127.0.0.1:8000/vote/
    #별칭 사용 : 'vote:index'
    path('', index, name='index'),
    #http://127.0.0.1:8000/숫자데이터/vote/
    path('<int:question_id>/', detail, name='detail'),
    #http://127.0.0.1:8000/vote/vote
    path('vote/',vote, name='vote'),
    #http://127.0.0.1:8000/vote/result/숫자데이터/
    path('result/<int:question_id>/',result, name='result'),
    path('qR/',questionResiger, name='questionResiger'),
    path('qU/<int:question_id>/', questionUpdate ,
         name='questionUpdate' ),
    path('qD/<int:question_id>/', questionDelete,
         name='questionDelete'),
    path('cD/<int:choice_id>/', choiceDelete,name='choiceDelete'),
    path('cR/',choiceRegister, name='choiceRegister'),
    path('cU/<int:cid>/',choiceUpdate,name='choiceUpdate')
    ]






