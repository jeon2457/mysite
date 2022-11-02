from django.urls import path
from . import views


# mysite/urls.py 에서도 추가작업을 해줘야한다.
urlpatterns = [
    path('', views.index, name='index'),
]
