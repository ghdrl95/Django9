"""
Django settings for Django9 project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy


#reverse_lazy : 기능은 reverse와 동일. 
#LOGIN_URL : login_required 데코레이터/ LoginReuquiredMixin 클래스를 통해 보여질 로그인페이지 주소
LOGIN_URL = reverse_lazy('auth:signin')#reverse('auth:signin')
#소셜로그인 완료 후 보여질 페이지의 주소
LOGIN_REDIRECT_URL = reverse_lazy('index')

#LOGIN_REDIRECT_URL : 로그인 후 이동할 페이지
#LOGOUT_REDIRECT_URL : 로그아웃 후 이동할 페이지
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#프로젝트가 위치한 경로를 의미함
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#python에 social-auth-app-django 설치해야함

#social-django 어플리케이션에서 사용하는 변수이름(사이트별로 고정된 변수 사용)
#구글에서 발급받은 클라이언트 ID
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='977782161476-98f9si7bbgcraaagdlbg92p9gniro4ip.apps.googleusercontent.com'
#구글에서 발급받은 보안 비밀
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='k0nWQrzuBAINBo98EIf8WFvg'
#console.developer.google.com 
#인증 관련 모듈을 추가하는 변수
AUTHENTICATION_BACKENDS = (
    #구글 인증관련 모듈 명시
    'social_core.backends.open_id.OpenIdAuth',#
    'social_core.backends.google.GoogleOpenId',#
    'social_core.backends.google.GoogleOAuth2',#
    #소셜로그인 정보를 Django의 User모델클래스에 매칭
    'django.contrib.auth.backends.ModelBackend',#
    )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xfa-3smm%#36d+@j1d%i4j&t@&13im@22d-@!alc!0zupnr$r)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#클라이언트가 웹서버에게 요청할 때 허용할 도메인이름 
#아무것도 적지않은경우 '127.0.0.1'로만 요청가능
ALLOWED_HOSTS = ['127.0.0.1','localhost', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark',
    'vote', #'bookmarkvote'
    'customlogin',
    #python에 social-auth-app-django 모듈이 설치되야함
    'social_django', #소셜로그인에 대한 어플리케이션
    'blog',
    #django-disqus 모듈을 설치해야함
    'disqus', #댓글 사이트와 연동하기 위한 어플리케이션
    'django.contrib.sites'
]
#disqus 사이트에서 발급받은 shortname 저장
DISQUS_WEBSITE_SHORTNAME = 'testdjango9'
#웹프로젝트별 개별적인 id값 설정
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django9.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',      #
                'social_django.context_processors.login_redirect',#
            ],
        },
    },
]

WSGI_APPLICATION = 'Django9.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#URL 주소로 파일 주소를 접근할때 사용하는 경로
#http://127.0.0.1:8000/files/ 로 시작하는 경로는 미디어파일을 불러오는 것으로 판단함
MEDIA_URL ='/files/'
#os.path.join(기존경로, 새경로) : 기존경로에 새경로를 붙인 문자열을 반환
#실제로 이미지/파일/동영상/한글/파워포인트이 저장되는 경로
#src폴더의 files폴더안에 미디어파일을 저장
MEDIA_ROOT =os.path.join(BASE_DIR,'files') 

#http://127.0.0.1:8000/files/1.jpg 요청시
#src/files/1.jpg 를 꺼냄


















