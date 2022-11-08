from django.contrib import admin
from .models import 아이디, Sale, Person, UserProfile

# 여기에 모델을 등록하세요.
# models.py에서 이곳과 연결시킨다.
admin.site.register(아이디)  # 아이디 등록
admin.site.register(Sale)  # Sale 등록
admin.site.register(Person)  # Person 등록
admin.site.register(UserProfile)  # UserProfile 등록


# 관리자모드 아이디: jeon2457 /  패스워드: 84..5
