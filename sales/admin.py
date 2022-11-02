from django.contrib import admin
from .models import 아이디, Sale, Person

# 여기에 모델을 등록하세요.
# models.py에서 이곳과 연결시킨다.
admin.site.register(아이디)  # 아이디 등록
admin.site.register(Sale)  # Sale 등록
admin.site.register(Person)  # Person 등록
