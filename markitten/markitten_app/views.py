import email
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from numpy import product
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count


# Create your views here.
@login_required(login_url='/login')
def home(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    p_form = Profile.objects.get(user=request.user)

    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ, "p_form": p_form}
    return render(request, 'markitten_app/Home.html', data)

def accessories(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ}
    return render(request, 'markitten_app/Peripherals.html', data)

def smartphones(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ}
    return render(request, 'markitten_app/Phones.html', data)

def desktops(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ}
    return render(request, 'markitten_app/Desktops.html', data)

def laptops(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ}
    return render(request, 'markitten_app/Laptops.html', data)

def monthlycatalog(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})

    data = {"items": items, "categ": categ}
    return render(request, 'markitten_app/monthlycatalog.html', data)

def product_details(request, pk):
    prod = Product.objects.get(id=pk)
    data = {"prod": prod } 
    
    form = ProdDetailsForm({"user": request.user.id, "item": prod.id,})
    data["form"] = form  
    return render(request, "markitten_app/productDetails.html", data)

def adminpanel(request):
    return render(request, 'markitten_app/adminPanel.html')

def productdetails(request):
    return render(request, 'markitten_app/productDetails.html')

@login_required(login_url='/login')
def profile(request):
    # User = get_user_model()
    p_form = Profile.objects.get(user=request.user)
    
    context = {
        'p_form': p_form
    }
    return render(request, 'markitten_app/profile.html', context)

@login_required(login_url='/login')
def editprofile(request):
    subscriptionTracker = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    

    context = {
        'u_form': u_form,
        'p_form': p_form,
        "subscription": subscriptionTracker
    }

    return render(request, 'markitten_app/editprofile.html', context)

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
            return redirect('profile')
        
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
    p_form = Profile.objects.get(user=request.user)

    context = {
        "p_form": p_form
    }

    return render(request, 'markitten_app/faq.html', context)

def about(request):
    p_form = Profile.objects.get(user=request.user)

    context = {
        "p_form": p_form
    }

    return render(request, 'markitten_app/about.html', context)

def changepassword(request):
    return render(request, 'markitten_app/changePassword.html')

def customersearch(request):
    customerUser = User.objects.all()
    customer = Profile.objects.all()

    context = {
        "customer" : customer,
        "customerUser": customerUser
    }

    return render(request, 'markitten_app/customerSearch.html', context)

def customerlocation(request):
    customer = Profile.objects.all()
    permanent_address_query = request.GET.get('permanent_address')

    if permanent_address_query != '' and permanent_address_query is not None:
        customer = customer.filter(permanent_address__icontains=permanent_address_query)

    context = {
        "customer" : customer
    }

    return render(request, 'markitten_app/customerLocation.html', context)

def productrating(request):
    return render(request, 'markitten_app/productrating.html')

def totalcustomers(request):
    maleCount = Profile.objects.filter(sex='Male').count()
    femaleCount = Profile.objects.filter(sex='Female').count()
    otherCount = Profile.objects.filter(sex='Male/Female').count()
    customer = Profile.objects.all()
    nationality_query = request.GET.get('nationality')
    # month = [i.month for i in Profile.objects.values_list('birthday', flat=True)]

    if nationality_query != '' and nationality_query is not None:
        customer = customer.filter(nationality__icontains=nationality_query)

    context = {
        "maleCount": maleCount,
        "femaleCount": femaleCount,
        "otherCount": otherCount,
        "customer": customer
        # "month": month
    }

    return render(request, 'markitten_app/totalCustomers.html', context)

def create(request):
    p_form = UserCreationForm()

    if request.method=='POST':
        p_form = UserCreationForm(request.POST)

        if (p_form.is_valid()):
            p_form.save()
            return redirect("customersearch")
    context = {
        "p_form" : p_form
    }
    return render(request, 'markitten_app/create.html', context)

def update(request, pk):
    customer = Profile.objects.get(id=pk)
    # customerUser = User.objects.get(id=pk)

    if request.method == 'POST':
        # u_form = UserUpdateForm(request.POST, instance=customerUser)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=customer)

        # if u_form.is_valid() and p_form.is_valid():
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            return redirect('customersearch')
    else:
        # u_form = UserUpdateForm(instance=customerUser)
        p_form = ProfileUpdateForm(instance=customer)
    
    context = {
        "customer": customer,
        # "customerUser": customerUser,
        # "u_form": u_form,
        "p_form" : p_form
    }

    return render(request, 'markitten_app/update.html', context)

def delete(request, pk):
    customer = Profile.objects.get(id=pk)
    customer.delete()

    return redirect('customersearch')