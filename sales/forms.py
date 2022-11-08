from django import forms  # forms 라이브러리를 가져온다.
from .models import Sale
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


''' # [방법-1]은 수동작업처리!
class SaleForm(forms.Form):  # 장고에서이미 짜여진 forms라이브러리를 불러오는것이다.

    first_name = forms.CharField()  # 첫번째 이름,()안에는 아무것도 넣으면안된다.
    last_name = forms.CharField()  # 마지막 이름
    age = forms.IntegerField(min_value=0)  # 나이 '''


# [방법-2]는 장고 라이브러리 폼을 사용해서 간결하다.
class SaleModelForm(forms.ModelForm):
    class Meta:  # Meta에서 모델이 뭔지를 알려준다.
        model = Sale  # 모델지정
        fields = (
            'first_name',
            'last_name',
            'age',
            'person',

        )


class 우리만의UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        fiele_classes = {'username': UsernameField}
