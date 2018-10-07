from django.contrib import admin

#현재폴더에 있는 models.py 파일에 BookMark 클래스를 사용할수있도록 추가 
from .models import BookMark as BM 
#bookmark 폴더에 있는 models.py 파일에 BookMark 클래스를 추가
#from bookmark.models import BookMark

#관리자사이트에서 BookMark 모델 클래스에 데이터를 추가/수정/삭제/열람을 할수있도록
#등록
admin.site.register(BM)