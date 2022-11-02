from django.shortcuts import render
from django.http import HttpResponse  # 응답 라이브러리


# 여기에서 함수를 만드세요.새로 시작한다면 urls.py모듈도 만들자.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
