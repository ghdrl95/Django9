from django.db import models
from django.contrib.auth.models import User
#Question 모델클래스
#질문 내용(200자 제한), 생성일
class Question(models.Model):
    name = models.CharField('질문 내용',max_length=200)
    #DateTimeField : 날짜/시간 저장하는 공간
    pub_date = models.DateTimeField('생성일')
    def __str__(self):
        return self.name
#Choice 모델클래스
#답변 내용, 투표수, 어느 질문에 연결?
class Choice(models.Model):
    name = models.CharField('답변 내용',max_length=100)
    #IntegerField : 정수값을 저장하는 공간
    vote = models.IntegerField('투표 수',default=0)
    #ForeignKey : 다른 모델클래스와 1:n 관계로 연결할 때 사용
    #연결된 Question객체가 지워질 경우 Choice 객체도 지워지도록 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

#댓글을 저장하는 모델 클래스
#사용자, 댓글내용, 생성일
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField('댓글내용',max_length=500)
    pub_date= models.DateTimeField('생성일',auto_now_add=True)













    
    
    
    
    