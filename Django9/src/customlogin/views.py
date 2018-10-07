from django.shortcuts import render
from .forms import SignupForm,LoginForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls.base import reverse

from django.contrib.auth import authenticate,login


# Create your views here.

#회원가입
def signup(request):
    if request.method == "GET":
        form = SignupForm()
        return render(request,'customlogin/signup.html',
                      {'form':form})
    elif request.method =="POST":
        form = SignupForm(request.POST)
        #사용자의 입력이 유효한지 확인(아이디중복, 비밀번호 형식 등)
        if form.is_valid():
            #is_valid() 함수 호출 후 cleaned_data 변수로 특정 입력을
            #추출할수 있음 
            #cleaned_data[키값]
            print(form.cleaned_data['username'])
            #form.save() #비밀번호를 암호화하는 과정이 생략되서 사용할수 없음
            #비밀번호 값이 일치하는지 확인
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                #유저생성
                new_user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'])
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name=form.cleaned_data['last_name']
                new_user.save()
            
                return HttpResponseRedirect(
                    reverse('index' ) )
            else:#비밀번호와 비밀번호확인이 틀린경우
                return render(request,'customlogin/signup.html',
                              {'form':form})
        else:   #유효한 값을 입력하지 않은경우
            return render(request,'customlogin/signup.html',
                          {'form':form})
#로그인
def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'customlogin/signin.html',{'form':form})
    elif request.method =="POST":
        #form.is_valid() 호출 후 cleaned_data를 사용할수 없음
        #is_valid() 호출 시 아이디 중복으로 False 값 반환됨
        #사용자가 아이디, 비밀번호를 잘못입력한 경우 사용자 입력을 유지하기 위해 폼클래스 객체 생성
        form = LoginForm(request.POST) 
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate(username, password) : User 모델클래스에 해당 ID와 Password를 가진 객체를 반환
        #객체가 없는경우 None 값 반환
        
        user = authenticate(username=username,password=password)
        if user is not None:
            #해당요청을 가진 클라이언트가 user객체로 로그인하는 작업을 수행
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,'customlogin/signin.html',
                          {'form':form, 'error':"아이디나 비밀번호가 맞지않습니다."})

from django.contrib.auth import logout        
#로그아웃        
def signout(request):
    #해당 요청을 한 클라이언트의 user 정보를 삭제
    logout(request)
    return HttpResponseRedirect(reverse('index'))














