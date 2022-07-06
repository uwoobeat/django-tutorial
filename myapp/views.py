from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

topics = [
    {'id':1, 'title':'routing', 'body':'Here comes the description of routing'},
    {'id':2, 'title':'view', 'body':'Here comes the description of view'},
    {'id':3, 'title':'model', 'body':'Here comes the description of model'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ""
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    #딕셔너리와 반복문을 통한 {ol} 처리

    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

#이렇게 웹 애플리케이션을 통해 로직만 수정하면 모든 웹페이지를 간단하게 수정할 수 있음

def index(request): #요청 내용이 들어있는 request 객체 받음
    article = """
        <h2>Here comes the description of the Django</h2>
        Hello, Django<br>
    """
    return HttpResponse(HTMLTemplate(article)) #Http로 요청에 대한 응답 리턴함

@csrf_exempt
def create(request):
    if request.method == "GET":
        article = """
            <form action="/create/" method="post">
                <h2>this is create page</h2>
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        return HttpResponse(HTMLTemplate(''))
    #name - 입력한 내용을 title로 전달
    #placeholder - 입력 도움말
    #<textarea> - 여러 줄 입력 전달
    #submit - 제출

    """
    querystring
    localhost:8000/read/1/
    localhost:8000/read/?id=1
    에서 ?id=1이 쿼리스트링이고 이 값이 read로 전달된다. 이 방식이 원래 쓰던 방법이고 표준임
    다른 값을 서버로 보내고 싶다면 쿼리스트링(질의 문자열)을 ?id=1&mode=1...처럼 이어붙여서 전송
    전자가 더 깔끔하기 때문에 최근에는 위의 것을 더 선호
    
    하지만 둘은 목적이 다르다. 위의 것은 브라우저가 서버로부터 GET하는 것이고
    아래 것은 브라우저가 서버에 있는 데이터를 변경하려는 작업임
    저 url에 접속할 때마다 데이터가 변경되므로, url에 쿼리스트링을 포함시키면 안됨
    그렇다면? POST라는 방식을 사용한다.

    우리가 위에서 보낸 요청(?뒤에 이어붙이는)은 GET 방식임.
    POST 방식은 이러한 데이터를 url이 아닌 header의 body 다음에 붙여서 요청
    header는 요청에 대한 추가 정보를 담고 있는 부분으로 
    """

def read(request, id):
    #HttpResponse에서는 HTML 코드가 들어갈 수 있다.
    #위에서 딕셔너리를 이용하여 {OL}을 처리했듯이 HTML 코드 전체를 함수화하여 처리 가능
    articleTopic = topics[int(id)-1]["title"]
    article = f"""
        <h2>Here comes the description of the {articleTopic}</h2>
        <p>Hello, {articleTopic}</p>
    """
    return HttpResponse(HTMLTemplate(article))


"""
라우팅 흐름을 파악해보자.
사용자가 /read/1로 접속하게 되면

1) 최상위 루트의 urls.py에서 include를 통해 myapps의 urls.py로 위임되고
2) read/<id>/로 위임된 것이 다시 views의 read 함수로 위임되어 
3) HttpResponse에 의한 응답값이 클라이언트에게 전달된다.
"""