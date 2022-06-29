from django.contrib import admin
from django.urls import path, include
from myapp import views #경로에 따라 views에 존재하는 각 함수로 위임해주기위해 import 


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read) 
    #<변수명>을 통해서 변할 수 있는 값을 표시
    #여기서의 id는 views의 read함수에서 두번째 파라미터를 통해 받을 수 있다
]

#두번째 파라미터로 views의 index 함수 전달하여 해당 경로 요청을 어떻게 처리할 것인지 확인 
