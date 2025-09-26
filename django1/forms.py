from django import forms

class userInput(forms.Form):
    fname=forms.CharField(label="firstname", max_length=40)
    mname= forms.CharField(max_length=30, required=False)
    lname=forms.CharField(label="lastname", max_length=50)
    email=forms.EmailField()
    num1=forms.CharField(max_length=50)
    num2=forms.CharField(max_length=60)
    num3=forms.CharField(max_length=60)

