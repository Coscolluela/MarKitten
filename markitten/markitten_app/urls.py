from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('leavecomplaint/', views.leavecomplaint, name="leavecomplaint"),
    path('leavereview/', views.leavereview, name="leavereview"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('productdetails/', views.productdetails, name="productdetails"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('faq/', views.faq, name="faq"),
    path('about/', views.about, name="about"),
]