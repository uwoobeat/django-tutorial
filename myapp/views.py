from django.shortcuts import render, HttpResponse

# Create your views here.
#urls로 전달된 path 처리

def index(request): #요청 내용이 들어있는 request 객체 받음
    return HttpResponse('Welcome!') #Http로 요청에 대한 응답 리턴함

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse(f'Read {id}')

"""
라우팅 흐름을 파악해보자.
사용자가 /read/1로 접속하게 되면

1) 최상위 루트의 urls.py에서 include를 통해 myapps의 urls.py로 위임되고
2) 다시 read/<id>/로 위임되어 views의 read 함수로 위임되어 
3) HttpResponse에 의한 응답값이 클라이언트에게 전달된다.
"""