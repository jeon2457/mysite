from django.db import models
from django.contrib.auth.models import AbstractUser  # 회원관리 모듈
from django.db.models.signals import post_save


# Create your models here.
# sales 앱은 판매에관한앱으로 데이타베이스를 만든다.


# 아이디 유저를 따로 만든다.
# setting.py에서 AUTH_USER_MODEL= 'sales.아이디' 라도 따로 추가해준다.
class 아이디(AbstractUser):
    pass


# DB에서 user(class Person)를 추가하면 UsePorfile도 같이 자동추가하려고
class UserProfile(models.Model):
    # 아이디가 지워지면 Person도 삭제된다.
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.username


# 회원가입
class Sale(models.Model):

    first_name = models.CharField(max_length=30)  # 첫번째 이름
    last_name = models.CharField(max_length=30)  # 마지막 이름
    age = models.IntegerField(default=0)  # 나이
    # Sale과 Person 과의 관계를 연결 관계가없을때는 삭제.
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"  # f: format 프롬프트상에 출력!


class Person(models.Model):
    # 아이디가 지워지면 Person도 삭제된다.
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)
    조직 = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.username


# 이렇게 만든 데이타베이스를 장고앱에서 인식을할수있게
# 해줘야한다. 먼저1단계로 프롬프트에서 py manage.py makemigrations 로
# 실행한다.
# 그다음 2단계로 py manage.py migrate(마이그레이션 적용) 한다.
# 이렇게해서 데이타베이스에 반영된다.


def 회원생성signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(회원=instance)


post_save.connect(회원생성signal, sender=아이디)
