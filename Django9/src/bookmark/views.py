from django.shortcuts import render
from .models import *
#View : 사용자의 요청에 따라 처리하고, HTML파일이나 새로운 URL주소를 전송함
#View 정의 시 함수 / 클래스 형태로 정의

#View 함수 정의시 첫번째 매개변수로 request 변수를 사용함
#request : 웹 클라이언트의 요청에 대한 정보를 가지고 있음
#ex) 로그인 정보, FORM(입력양식) 값, 등

#메인페이지
def index(request):
    #render(request, HTML문서 위치(문자열), 템플릿에 전달할 값(사전형))
    #현재 요청을 한 웹 클라이언트에게 bookmark폴더에 있는 index.html 파일을 전송
    #사전형 : {키 : 값 ,} 키 : 숫자,문자열   값 :상수,문자열,변수,객체,리스트,튜플,사전
    #변수명[키]
    #탬플릿에 사전형 데이터를 전송하면 키에 해당하는 값을 변수처럼 사용
    return render(request, 'bookmark/index.html', 
                  {'hello':'world', 'list':[1,2,3] } )

#BookMark 모델클래스에 저장된 객체들을 HTML문서에 출력
def booklist(request):
    #BookMark 객체 검색
    #get() : 객체 하나만 가져오기
    #all() : 객체 전체 가져오기
    #데이터 베이스에 저장된 BookMark 객체들을 모두 추출해 리스트형태로 반환하는 함수
    obj = BookMark.objects.all() 
    #탬플릿 전달
    return render(request,'bookmark/booklist.html',
                  { 'list': obj })
    
#웹 클라이언트가 선택한 북마크 객체를 화면에 출력하는 뷰함수
#bookmark_id : 해당 id값을 가진 객체를 추출하기 위한 매개변수
def bookdetail(request, bookmark_id ):
    #get함수 : 해당 모델클래스에서 하나의 객체를 추출
    #get함수의 인자값은 해당 모델클래스의 변수명을 사용
    
    #BookMark 모델클래스의 객체들 중 id 변수에 들어있는 값이
    #bookmark_id 값과 동일한 객체 한개를 추출
    obj = BookMark.objects.get(id = bookmark_id) #해당조건을 만족하는 객체 반환
    #만약, 해당 조건을 만족하는 객체가 없는경우 -> 서버오류 판단해 500번대 에러가 뜸
    
    return render(request,'bookmark/bookdetail.html',
                  { 'obj': obj })







    
    
    
    
    