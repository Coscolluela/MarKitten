from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('adminpanel/', views.adminpanel, name="adminpanel"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('leavecomplaint/', views.leavecomplaint, name="leavecomplaint"),
    path('leavereview/', views.leavereview, name="leavereview"),
    path('login/', views.signin, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),
    path('productdetails/', views.productdetails, name="productdetails"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('faq/', views.faq, name="faq"),
    path('about/', views.about, name="about"),
    path('customersearch/', views.customersearch, name="customersearch"),
    path('customerlocation/', views.customerlocation, name="customerlocation"),
    path('productrating/', views.productrating, name="productrating"),
    path('totalcustomers/', views.totalcustomers, name="totalcustomers"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)