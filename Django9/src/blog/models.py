from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
#카테고리
class PostType(models.Model):
    name = models.CharField('카테고리', max_length=100)
    def __str__(self):
        return self.name

#from django.contrib.auth.models import User
from django.conf import settings
#글 (글제목, 글내용, 작성자(외래키), 작성일, 카테고리(외래키) )
class Post(models.Model): # ~25분까지
    #카테고리(type) : ForeignKey. PostType 모델클래스와 연동
    type = models.ForeignKey(PostType,on_delete=models.PROTECT)
    #외래키 설정 시 on_delete에 넣을 수 있는 값
    #models.CASCADE : 연결된 객체가 삭제되면 다같이 삭제되는 것
    #models.PROTECT : 연결된 객체가 삭제되지 않도록 막는 역할
    #models.SET_NULL : 연결된 객체가 삭제되면 null값을 가지는 역할
    #models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 객체와 연결되는 역할
    #models.SET() : 연결된 객체가 삭제되면 특정함수로 새로운 객체를 찾아 연결하는 역할
    #글 제목(headline) : CharField. 글자수 200자 제한
    headline = models.CharField('제목', max_length=200)
    #글 내용(content) : TextField(글자수 제한 없는 텍스트저장 공간).
    content = models.TextField('내용')
    #작성자(author) : ForeignKey. Django.auth.models.User 모델클래스와 연동
    #settings.AUTH_USER_MODEL : 현재 웹서버에 설정된 모델클래스를 의미
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #작성일(pub_date) : DateTimeField. auto_now_add=True
    pub_date = models.DateTimeField('작성일',auto_now_add=True)
    class Meta: #모델 클래스도 Meta 클래스를 정의해서 추가적인 정렬, 정보를 제공
        #ordering : 모델클래스에서 사용하는 변수명을 입력해 정렬하는 방식을 명시
        #기본적으로 오름차순으로 정렬함. 변수명앞에 '-' 기호를 붙이면 내림차순으로 정렬
        ordering = ['-id'] 
        #관리자 사이트에서 해당 모델클래스의 이름을 변경
        verbose_name = '글'

#이미지 저장 Post(외래키), 이미지 저장 공간 
class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    #ImageField() : 이미지의 경로를 저장하는 필드
    #upload_to : 이미지 저장시 어떤 폴더이름으로 분류할지 지정하는 매개변수
    # %Y : 해당 서버의 년도
    # %m : 해당 서버의 월
    # %d : 해당 서버의 일 
    image = models.ImageField('이미지파일', upload_to = "images/%Y/%m/%d" )
    #객체 삭제 시 image에 저장한 파일 경로의 파일 삭제 처리
    def delete(self, using=None, keep_parents=False):
        #image변수에 저장된 경로의 파일을 지우는 작업
        #왜? PostImage객체가 지워질때 image변수가 가르키는 경로의 파일이 지워지지 않음
        #ImageField/FileField 사용시 객체가 삭제될때 호출되는 delete함수를 오버라이딩해서
        #해당 객체를 수동으로 지우는 작업(delete함수 호출)을 수행해야함
        self.image.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)
#파일 저장
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #FileField() : 파일의 경로를 저장하는 필드
    file = models.FileField('파일', upload_to = 'files/%Y/%m/%d')
    #객체 삭제시 file에 저장한 파일 경로에 해당하는 파일을 삭제하는 처리
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)














