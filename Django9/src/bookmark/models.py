from django.db import models

# 모델 클래스 정의
# 모델(Model) : 데이터베이스에 데이터를 저장할 때, 어떠한 형식으로 저장할지
#              관리하는 부분
#models.Model : 장고에서 제공하는 Model 클래스, 해당 클래스를 상속받아야만
#               Model의 기능을 할 수 있음
#북마크 모델 클래스
#북마크 이름, URL 주소 
class BookMark(models.Model):
    #해당 모델클래스에 저장할 값을 정의할 때, 클래스 내의 변수 정의
    #변수 정의 시 xxxxField 클래스의 객체를 변수에 대입해 어떤 값을 저장할지
    #정의 함
    #CharField() : 글자수 제한이 있는 문자열을 저장하는 공간 정의
    #URLField() : 인터넷 주소를 저장하는 공간 정의
    bookname = models.CharField(max_length=100)
    bookurl = models.URLField()
    #객체를 출력할 때 표현방식을 처리하는 함수
    def __str__(self):
        return self.bookname
     
    
    
    
    
    
    
    
    
    
    
    