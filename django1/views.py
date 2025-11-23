from django.shortcuts import HttpResponse, render
from . import forms
def home(req):
    return HttpResponse("I am from home method")

def homewebpage(req):
    return render(req, 'home.html')

def getForm(req):
    try:
        # a = req.GET.get("first", None)
        # b = req.GET.get("second", None)

        # or 

        a= ""
        b= ""
        a = req.GET["first"]
        b = req.GET["second"]

    except:
        pass
    return render(req, 'getForm.html', {"value1": a, "value2": b})

def postForm(req):
    try:
        a = req.POST.get("first")
        b = req.POST.get("second")
    except:
        pass
    return render(req, 'postForm.html', {"value1": a, "value2": b})

def userInput(req):
    fn = forms.userInput()
    n1 = n2 = n3 = n4 = ""
    total=0
    if req.method == "POST":
        try:
            n1 = req.POST.get("fname", "")
            n2 = req.POST.get("mname", "")
            n3 = req.POST.get("lname", "")
            n4 = req.POST.get("email", "")
            n5 = int(req.POST.get("num1", 0))
            n6 = int(req.POST.get("num2", 0))
            n7 = int(req.POST.get("num3", 0))
            total = n5 + n6 + n7
        except:
            pass

    data={'fname': n1, "mname": n2, "lname": n3, "email":n4, 'total': total, "form": fn}
    return render(req, "Djangoform.html",data)