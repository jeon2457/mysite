from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Question(models.Model):  # 질문DB
    question_text = models.CharField(max_length=200)   # 질문내용
    pub_date = models.DateTimeField('date published')  # 생성날짜

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):  # 선택DB
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 위의 설문조사 데이타베이스를 settings.py에서 등록해준다.
