"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    다른 URL로 위임하려면
"""
from django.contrib import admin
from django.urls import path, include #다른 app으로의 위임 위해 include import함
# http://127.0.0.1/
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1

#urlpatterns라는 리스트를 반드시 정의하여 라우팅 정보 명시해야 함
urlpatterns = [
    path('admin/', admin.site.urls), #admin으로 접속 시 관리자 설정으로 라우팅
    path('', include('myapp.urls'))
    # include(--)는 myapp의 urls.py로 위임하여 라우팅
    # 첫번째 인자에 빈 문자열 ''을 전달하면 else 처리하여 라우팅
]
