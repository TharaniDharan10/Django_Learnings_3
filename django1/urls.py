from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("djangoclass.urls")),
    path('home/', views.home),
    path('homeweb/', views.homewebpage),
    path('getform/', views.getForm),
    path('postform/', views.postForm),
    path('djangoform/', views.userInput)

]
