"""mysite URL 구성

'urlpatterns' 목록은 URL을 보기로 라우팅합니다. 자세한 내용은 다음을 참조하십시오.
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
예:
기능 보기
    1. 가져오기 추가: my_app 가져오기 보기에서
    2. urlpatterns에 URL 추가: path('', views.home, name='home')
클래스 기반 보기
    1. import 추가: from other_app.views import 홈
    2. urlpatterns에 URL 추가: path('', Home.as_view(), name='home')
다른 URLconf 포함
    1. include() 함수를 가져옵니다. django.urls에서 include, 경로 가져오기
    2. urlpatterns에 URL 추가: path('blog/', include('blog.urls'))
"""
# (참고동영상): 기초부터 제작하는 파이썬 장고(Python Django) 프로젝트

from django.contrib import admin    # 관리자페이지를 이용하기위함
from django.urls import path
from django.urls.conf import include  # sales.views에서 홈페이지를 불러온다.
from sales.views import 첫화면,첫화면view, 회원가입View
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # sales앱의 views.py에있는 홈페이지 함수를 실행한다.
    # "홈페이지"를 sales앱의 urls.py로 찾아간다.
    # include()URL에서 해당 지점까지 일치하는 부분을 잘라내고 추가 처리를 위해 포함된 URLconf에 나머지 문자열을 보냅니다.
    path('', 첫화면view.as_view()),
    path('홈페이지/', include('sales.urls', namespace="홈페이지")),
    path('polls/', include('polls.urls')),  # polls의 urls도 포함시킴.
    path('로그인/', LoginView.as_view(), name='로긴'),
    path('로그아웃/', LoginView.as_view(), name='록아웃'),
    path('회원가입/', 회원가입View.as_view(), name='가입')




]
