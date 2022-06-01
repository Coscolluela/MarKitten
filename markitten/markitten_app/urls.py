from re import template
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MyPasswordSentForm
from django.http import HttpResponseRedirect

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
    path('product_details/<str:pk>/', views.product_details, name="product_details"),
    path('changepassword/', 
        PasswordChangeView.as_view(
			template_name = 'markitten_app/changePassword.html',
			success_url = reverse_lazy('profile'),
			form_class = MyPasswordChangeForm
        ), name="changepassword"),
    path('forgotpassword/', PasswordResetView.as_view(
        template_name = 'markitten_app/passchange.html',
		form_class = MyPasswordResetForm
	), name = 'reset_password'),
    
    path('forgotpassword_sent/', PasswordResetView.as_view(
        template_name = 'markitten_app/forgotsent.html'), name = 'password_reset_done'),
    
    path('forgotpassword/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name = 'markitten_app/passconfirm.html'), name = 'password_reset_confirm'),
    path('forgotpassword_complete/', PasswordResetCompleteView.as_view(
        template_name = 'markitten_app/forgotdone.html'), name = 'password_reset_complete'),
    path('faq/', views.faq, name="faq"),
    path('about/', views.about, name="about"),
    path('customersearch/', views.customersearch, name="customersearch"),
    path('customerlocation/', views.customerlocation, name="customerlocation"),
    path('productrating/', views.productrating, name="productrating"),
    path('totalcustomers/', views.totalcustomers, name="totalcustomers"),
    path('Accessories/', views.accessories, name="Accessories"),
    path('Smartphones/', views.smartphones, name="Smartphones"),
    path('desktops/', views.desktops, name="desktops"),
    path('Laptop/', views.laptops, name="Laptop"),
    path('monthlycatalog/', views.monthlycatalog, name="monthlycatalog"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>', views.update, name="update"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('addreview/<str:pk>/', views.addreview, name="addreview"),
    path('addcomplaint/<str:pk>/', views.addcomplaint, name="addcomplaint"),
    path('product_complaints/<str:pk>/', views.product_complaints, name="product_complaints"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)