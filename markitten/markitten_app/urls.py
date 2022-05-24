from re import template
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MyPasswordSentForm

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
    path('changepassword/', 
        PasswordChangeView.as_view(
			template_name = 'markitten_app/changePassword.html',
			success_url = reverse_lazy('profile'),
			form_class = MyPasswordChangeForm
        ), name="changepassword"),
    path('forgotpassword/', auth_views.PasswordResetView.as_view(
        template_name = 'markitten_app/passchange.html',
		form_class = MyPasswordResetForm
	), name = 'reset_password'),
    path('forgotpassword_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name = ('markitten_app/forgotsent.html')), name = 'password_reset_done'),
    path('forgotpassword/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'markitten_app/passconfirm.html',
        form_class = MyPasswordSentForm), name = 'password_reset_confirm'),
    path('forgotpassword_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('faq/', views.faq, name="faq"),
    path('about/', views.about, name="about"),
    path('customersearch/', views.customersearch, name="customersearch"),
    path('customerlocation/', views.customerlocation, name="customerlocation"),
    path('productrating/', views.productrating, name="productrating"),
    path('totalcustomers/', views.totalcustomers, name="totalcustomers"),
    path('peripherals/', views.peripherals, name="peripherals"),
    path('phones/', views.phones, name="phones"),
    path('desktops/', views.desktops, name="desktops"),
    path('laptops/', views.laptops, name="laptops"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)