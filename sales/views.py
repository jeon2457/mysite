# (참고동영상): 기초부터 제작하는 파이썬 장고(Python Django) 프로젝트

from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.http import HttpRequest
from .models import Sale, Person  # 딕셔너리로 사용하기위함!
# from .forms import SaleForm  # forms.py와 연결[방법-1]은 주석처리!
# forms.py와 연결[방법-2]/ SaleForm이 아닌
from .forms import SaleModelForm, 우리만의UserCreationForm
# SaleModelForm으로 사용하면 더 간단하게 폼을 만들수있다.
from django.views import generic


# 여기에서 보기(뷰페이지)를 만드세요.
# 호출하려면 URL에 매핑해야하며 이를위해서 urls.py를 만들고 연결시켜줘야한다.
# 그리고 index.html파일을 만들어놓은 상태이다.

class 회원가입View(generic.CreateView):
    template_name = "newfolder/회원가입/가입.html"
    form_class = 우리만의UserCreationForm()

    def get_success_url(self):
        return reverse("로긴")


def 첫화면(request):  # 상위 urls.py에서 추가작업(import/path)
    return render(request, "첫화면.html")


def 세일목록(request):  # 함수명을 세일목록 으로 했다.
    # 바깥쪽 templates폴더를 새로만든것을 mysite앱의 settings.py속의 templatse에서 'DIRS'path를 걸어놓았다.
    # 드실분 = 아이디.objects.all()  # DB의 아이디 정보를 모두가져온다.
    사람 = Sale.objects.all()  # Sale에 있는 모든 객체를 가져와서 사람 변수에 담는다.
    context = {    # 딕셔너리형태의 "사람키": 사람 을 context변수에 담는다.
        # "메뉴명": "짜장",
        # "가격": "700원",
        # "손님": 드실분  # index.html에서 추가기입
        "사람키": 사람
    }

    # 세번째 파라미터로 context를 사용했다.dictionary 를 의미한다.
    # return render(request, "index.html", context)
    return render(request, "newfolder/세일목록.html", context)


def 세일상세(request, pk):

    사람 = Sale.objects.get(id=pk)

    context = {
        "사람키": 사람
    }

    # return HttpResponse("여기 상세 정보입니다.") # 간략하게 페이지뷰 확인차원에서 사용!
    return render(request, "newfolder/세일상세.html", context)  # 세일상세.html파일을
    # sales-templates-newfolder폴더안에 새로 만들어준다.


''' def 세일입력(request):   # [방법-1]은 수동작업처리!
    print(request.POST)  # 프롬프트에서 출력을 확인하기위함이다.
    폼 = SaleForm()
    if request.method == "POST":  # 만약에 요청한 메소드가 POST라면
        print("포스트 메소드로 왔네요")
        폼 = SaleForm(request.POST)
        if 폼.is_valid():  # 유효성검사
            print("유효하네요")
            print(폼.cleaned_data)  # cleaned_data로 저장
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            Sale.objects.create(  # 만들어서 DB로 저장
                first_name=first_name,
                last_name=last_name,
                age=age,
                person=person
            )
            print("세일이 입력 되었습니다.")

            return redirect("/홈페이지")  # 전송(submit)버튼클릭하면 다시 홈페이지로 넘어간다.
    context = {
        "폼키": 폼
    }
    return render(request, "newfolder/세일입력.html", context) '''


def 세일입력(request):   # [방법-2] 장고 라이브러리 폼을 사용해서 간결하다.
    print(request.POST)  # 프롬프트에서 출력을 확인하기위함이다.
    폼 = SaleModelForm()
    if request.method == "POST":  # 만약에 요청한 메소드가 POST라면

        폼 = SaleModelForm(request.POST)  # 방법-1에 비해서 SaleModelForm은 형식이 간단하다.
        # forms.py에서 방법-2로 먼저 정의해 놓았기때문이기도하다.
        if 폼.is_valid():  # 유효성검사
            폼.save()

            # 전송(submit)버튼클릭하면 다시 홈페이지로 넘어간다.
            return redirect("/홈페이지/")

    context = {
        "폼키": 폼
    }

    return render(request, "newfolder/세일입력.html", context)


''' # 세일_업데이트 함수를 만들면 urls.py에서 연결시켜줘야한다.
def 세일_업데이트(request, pk):    # [방법-1]
    사람 = Sale.objects.get(id=pk)

    폼 = SaleForm()
    if request.method == "POST":  # 만약에 요청한 메소드가 POST라면

        폼 = SaleForm(request.POST)
        if 폼.is_valid():  # 유효성검사

            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            사람.first_name = first_name
            사람.last_name = last_name
            사람.age = age
            사람.save()

            return redirect("/홈페이지")  # 전송(submit)버튼클릭하면 다시 홈페이지로 넘어간다.

    context = {
        "폼키": 폼,
        "사람키": 사람
    }

    return render(request, "newfolder/세일_업데이트.html", context)
 '''


# 세일입력되어 있는 데이타를 재수정하고자할때 사용!
def 세일_업데이트(request, pk):  # [방법-2]
    사람 = Sale.objects.get(id=pk)

    폼 = SaleModelForm(instance=사람)
    if request.method == "POST":  # 만약에 요청한 메소드가 POST라면

        폼 = SaleModelForm(request.POST, instance=사람)
        if 폼.is_valid():  # 유효성검사

            폼.save()

            return redirect("/홈페이지")  # 전송(submit)버튼클릭하면 다시 홈페이지로 넘어간다.

    context = {  # 데이터를 보여주기위해 사용
        "폼키": 폼,
        "사람키": 사람
    }

    return render(request, "newfolder/세일_업데이트.html", context)


def 세일_지우기(request, pk):   # [방법-2] 장고 라이브러리 폼을 사용해서 간결하다.
    사람 = Sale.objects.get(id=pk)
    사람.delete()  # 해당 고객을 삭제한다.

    return redirect("/홈페이지")  # 삭제하면 자동으로 홈페이지로 돌아간다.
