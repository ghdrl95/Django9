"""Django9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from bookmark.views import *
#urlpatterns : 등록된 URL을 관리하는 변수
#URL등록시 path()함수를 이용해 urlpatterns의 요소를 추가
#path(URL주소(문자열), 뷰함수이름)
#웹서버 실행시 나오는 도메인주소(127.0.0.1:8000)은 기본값 부여 
urlpatterns = [
    #http://127.0.0.1:8000/admin 로 접근시 관리자사이트 호출
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000 로 접근시 index함수 호출
    path('', index, name='index'  ),
    #http://127.0.0.1:8000/list 로 접근시 booklist 함수 호출
    path('list/', booklist, name='booklist' ),
    #http://127.0.0.1:8000/숫자데이터/ 로 접근시 bookdetail함수 호출
    #이 때, 숫자데이터에 값은 bookmark_id 매개변수에 들어감
    path('<int:bookmark_id>/', bookdetail, name='bookdetail'),
    #주소에 http://127.0.0.1:8000/vote 가 포함이 되어있으면, vote폴더안에
    #있는 urls.py 에 등록된 url을 사용 
    path('vote/', include("vote.urls")),
    #주소에 http://127.0.0.1:8000/auth/ 가 적힌 URL들은
    #customlogin폴더에 있는 urls 파일이 관리
    path('auth/', include("customlogin.urls")),
    
    # 'social'이라는 이름으로 그룹명을 변경 (app_name 변수 무시)
    path('oauth/',include("social_django.urls", namespace="social") ),
    path('blog/',include("blog.urls"))
]
#이미지 관련 처리를 위해 Pillow 모듈 설치
from django.conf import settings
from django.conf.urls.static import static
#URL 요청과 실제 파일 매칭을 등록
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











