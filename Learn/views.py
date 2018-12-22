from django.shortcuts import render,HttpResponse,redirect
import time,datetime
from Learn.models import Staff
from django.views import View

# Create your views here.


def index(request):
    inUID=request.session.get("LogID",None)
    if not inUID:
        Formtime=time.ctime()
        return render(request, "BaseHtml.html")
    else:
        return render(request, "BaseHtml.html",locals())


def personalInfoHandler(request,pWID):
    if request.method == "POST":
        return "Success"
    return render(request, "SignIn.html", locals())


def login(request):

    return HttpResponse("Login")
    pass



def staff_signin(request):
    if request.method == 'GET':
            return render(request, "SignIn.html", locals())
    else:
        if request.method == 'POST':
            print(request.COOKIES)
            print(request.session)

            for i in request.session:
                print(i)
            print(request.path)
            print(request.POST)
            inUID= request.POST.get("UID", None)
            request.session["LogID"]=inUID
            ret = render(request, "BaseHtml.html", locals())
            ret.set_cookie("name", inUID)

            return render(request, "BaseHtml.html",locals())
    pass


def staff_signup(request):
    if request.method == 'GET':
        print("CookieDate:", request.COOKIES)
        return render(request, "SignUp.html", locals())
    else:
        if request.method == 'POST':
            print(request.path)
            print(request.POST)
            """
            LoginID = models.CharField(max_length=20)
            PassWord = models.CharField(max_length=20)
            Name = models.CharField(max_length=10)
            Sex = models.BooleanField(default=True)
            EmailAdd = models.CharField(max_length=30,default="")
            TelNum = models.IntegerField(default=-1)
            Birthday = models.DateField(max_length=20, null=True)
            JoinTime = models.DateField()
            LessonCover = models.IntegerField(default=0)                      
            """
            try:
                s = Staff(LoginID=request.POST["iUID"],
                          PassWord=request.POST["pwd"],
                          Name=request.POST["name"],
                          Sex=True if request.POST["gender"] == "1" else False,
                          EmailAdd=request.POST["email"],
                          TelNum=request.POST["tel"],
                          Birthday=request.POST["birth"],
                          JoinTime=request.POST["join_day"],
                                                   )
                print(s)
                print(s.LoginID)
                print(s.Birthday)
                print(s.JoinTime)
                print(s.Name)
                print(s.Sex)
                print(s.TelNum)
                print(s.EmailAdd)
                Info = '注册成功'
                s.save()
            except Exception as e:
                Info = '注册失败'
                print(e)
            return HttpResponse(Info)

'''
Below is class url CBV

'''


class MyLesson(View):

    def dispatch(self, request, *args, **kwargs):

        ret = super(MyLesson, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):

        return render(request, "lessonPage.html", locals())

    def post(self,request):
        pass

