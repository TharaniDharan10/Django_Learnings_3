from contextlib import nullcontext
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
    total=0
    try:
        n1=req.POST["fname"]
        n2=req.POST["mname"]
        n3=req.POST["lname"]
        n4=req.POST["email"]
        n5=int(req.POST["num1"])
        n6=int(req.POST["num2"])
        n7=int(req.POST["num3"])
        total=n5+n6+n7
    except:
        pass

    data={'fname': n1, "mname": n2, "lname": n3, "email":n4, 'total': total}
    return render(req, "Djangoform.html",data)