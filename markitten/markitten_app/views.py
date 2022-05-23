from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'markitten_app/Home.html')

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
    return render(request, 'markitten_app/signup.html')

def login(request):
    return render(request, 'markitten_app/login.html')

def faq(request):
    return render(request, 'markitten_app/faq.html')

def about(request):
    return render(request, 'markitten_app/about.html')

def changepassword(request):
    return render(request, 'markitten_app/changePassword.html')