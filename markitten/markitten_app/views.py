import email
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import *
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'markitten_app/Home.html')

def adminpanel(request):
    return render(request, 'markitten_app/adminPanel.html')

def productdetails(request):
    return render(request, 'markitten_app/productDetails.html')

def profile(request):
    
    return render(request, 'markitten_app/profile.html')

def editprofile(request):
    return render(request, 'markitten_app/editprofile.html')

def leavecomplaint(request):
    return render(request, 'markitten_app/leaveComplaint.html')

def leavereview(request):
    return render(request, 'markitten_app/leaveReview.html')

def signup(request):
    form = UserForm()

    if(request.method == "POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            return redirect('/')
        
    data = {"form" : form}
    return render(request, 'markitten_app/signup.html', data)

def signin(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print("Login was successful")
            return redirect('/')
        else:
            print("Login failed")
            messages.error(request, "Incorrect password or email.")

    return render(request, 'markitten_app/login.html')

def signout(request):
    logout(request)
    return redirect('/')

def faq(request):
    return render(request, 'markitten_app/faq.html')

def about(request):
    return render(request, 'markitten_app/about.html')

def changepassword(request):
    return render(request, 'markitten_app/changePassword.html')