'''
Created on 2018. 9. 30.

@author: user
'''
from django.urls import path
from .views import signup,signin,signout
app_name ='auth'
urlpatterns=[#34
    #127.0.0.1:8000/auth/signup
    path('signup/',signup,name="signup"),
    path('login/',signin,name="signin"),
    path('logout/',signout,name="signout")
    ]