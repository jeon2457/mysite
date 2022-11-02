from django.urls import path
from django.contrib import admin  # 관리자페이지를 이용하기위함

from .views import 세일목록, 세일상세, 세일입력, 세일_업데이트  # views.py def"홈페이지" 함수를 가져온다.
from .views import 세일_지우기

app_name = "홈페이지-test..."

urlpatterns = [
    path('', 세일목록, name='목록'),
    # pk(primary key); model에서 찍어낸 수많은 객체들을 구분할 수 있는 구분자
    path('<int:pk>/', 세일상세, name='상세'),  # int; 정수형
    path('<int:pk>/업데이트/', 세일_업데이트, name='업뎃'),
    path('<int:pk>/지우기/', 세일_지우기, name='지우기'),
    path('make/', 세일입력, name='생성'),


]
