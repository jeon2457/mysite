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

from django.contrib import admin    # 관리자페이지를 이용하기위함
from django.urls import path
from django.urls.conf import include  # sales.views에서 홈페이지를 불러온다.


urlpatterns = [
    path('admin/', admin.site.urls),
    # sales앱의 views.py에있는 홈페이지 함수를 실행한다.
    # "홈페이지"를 sales앱의 urls.py로 찾아간다.
    # include()URL에서 해당 지점까지 일치하는 부분을 잘라내고 추가 처리를 위해 포함된 URLconf에 나머지 문자열을 보냅니다.
    path('홈페이지/', include('sales.urls', namespace="홈페이지")),
    path('polls/', include('polls.urls')),  # polls의 urls도 포함시킴.

]
