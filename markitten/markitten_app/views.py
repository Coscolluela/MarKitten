import email
import math
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
from datetime import date
from django.db.models.expressions import RawSQL

# Create your views here.
@login_required(login_url='/login')
def home(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []

    name_query = request.GET.get('name')

    if name_query != '' and name_query is not None:
        prods = prods.filter(name__icontains=name_query)

    p_form = Profile.objects.get(user=request.user)

    prodrating = {}
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})
        
        comments = prod.comment_set.all().order_by("-created_at")
        if ( len(comments) != 0 ):
            overall_rating = 0
            for comment in comments:
                overall_rating += comment.rating 
            overall_rating = overall_rating/len(comments)
            prodrating[prod.id] = round(overall_rating)
        else: 
            prodrating[prod.id] = 0

    data = {"items": items, "categ": categ, "p_form": p_form, "prodrating": prodrating}
    return render(request, 'markitten_app/Home.html', data)

def accessories(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []

    name_query = request.GET.get('name')

    if name_query != '' and name_query is not None:
        prods = prods.filter(name__icontains=name_query)

    p_form = Profile.objects.get(user=request.user)

    prodrating = {}
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})
        
        comments = prod.comment_set.all().order_by("-created_at")
        if ( len(comments) != 0 ):
            overall_rating = 0
            for comment in comments:
                overall_rating += comment.rating 
            overall_rating = overall_rating/len(comments)
            prodrating[prod.id] = round(overall_rating)
        else: 
            prodrating[prod.id] = 0

    data = {"items": items, "categ": categ, "p_form": p_form, "prodrating": prodrating}
    return render(request, 'markitten_app/Peripherals.html', data)

def smartphones(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []

    name_query = request.GET.get('name')

    if name_query != '' and name_query is not None:
        prods = prods.filter(name__icontains=name_query)

    p_form = Profile.objects.get(user=request.user)

    prodrating = {}
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})
        
        comments = prod.comment_set.all().order_by("-created_at")
        if ( len(comments) != 0 ):
            overall_rating = 0
            for comment in comments:
                overall_rating += comment.rating 
            overall_rating = overall_rating/len(comments)
            prodrating[prod.id] = round(overall_rating)
        else: 
            prodrating[prod.id] = 0

    data = {"items": items, "categ": categ, "p_form": p_form, "prodrating": prodrating}
    return render(request, 'markitten_app/Phones.html', data)

def desktops(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []

    name_query = request.GET.get('name')

    if name_query != '' and name_query is not None:
        prods = prods.filter(name__icontains=name_query)

    p_form = Profile.objects.get(user=request.user)

    prodrating = {}
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})
        
        comments = prod.comment_set.all().order_by("-created_at")
        if ( len(comments) != 0 ):
            overall_rating = 0
            for comment in comments:
                overall_rating += comment.rating 
            overall_rating = overall_rating/len(comments)
            prodrating[prod.id] = round(overall_rating)
        else: 
            prodrating[prod.id] = 0

    data = {"items": items, "categ": categ, "p_form": p_form, "prodrating": prodrating}
    return render(request, 'markitten_app/Desktops.html', data)

def laptops(request):
    prods = Product.objects.all()
    categ = Category.objects.all()
    items = []

    name_query = request.GET.get('name')

    if name_query != '' and name_query is not None:
        prods = prods.filter(name__icontains=name_query)

    p_form = Profile.objects.get(user=request.user)

    prodrating = {}
    for prod in prods:
        form = ProdDetailsForm({"user": request.user.id, "item": prod.id})
        items.append({"prod": prod, "form": form})
        
        comments = prod.comment_set.all().order_by("-created_at")
        if ( len(comments) != 0 ):
            overall_rating = 0
            for comment in comments:
                overall_rating += comment.rating 
            overall_rating = overall_rating/len(comments)
            prodrating[prod.id] = round(overall_rating)
        else: 
            prodrating[prod.id] = 0

    data = {"items": items, "categ": categ, "p_form": p_form, "prodrating": prodrating}
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

    comments = prod.comment_set.all().order_by("-created_at")
    if ( len(comments) != 0 ):
        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
        overall_rating = overall_rating/len(comments)
        data = {'prod': prod, 'comments':comments, 'overall_rating': round(overall_rating), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer(),}
    else: 
        data = {'prod': prod, 'rating_floor' : 0 }

    # commentform = CommentForm({"user" : request.user.id, "product" : product.id, "comment" : "", "rating" : "0"})
    # data["commentform"] = commentform
    data["totalreviews"] = len(comments)
    
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
    youngadult = 0
    maleyoungadult = 0
    femaleyoungadult = 0
    pendingyoungadult = 0
    adult = 0
    maleadult = 0
    femaleadult = 0
    pendingadult = 0
    senior = 0
    malesenior = 0
    femalesenior = 0
    pendingsenior = 0
    pending = 0
    malepending = 0
    femalepending = 0
    pendingunknown = 0

    if nationality_query != '' and nationality_query is not None:
        customer = customer.filter(nationality__icontains=nationality_query)

    for cust in customer:
        if cust.classification == 'Young Adult':
            youngadult = youngadult + 1
            if cust.sex == 'Male':
                maleyoungadult = maleyoungadult + 1
            elif cust.sex == 'Female':
                femaleyoungadult = femaleyoungadult + 1
            else:
                pendingyoungadult = pendingyoungadult + 1
        elif cust.classification == 'Adult':
            adult = adult + 1
            if cust.sex == 'Male':
                maleadult = maleadult + 1
            elif cust.sex == 'Female':
                femaleadult = femaleadult + 1
            else:
                pendingadult = pendingadult + 1
        elif cust.classification == 'Senior Citizen':
            senior = senior + 1
            if cust.sex == 'Male':
                malesenior = malesenior + 1
            elif cust.sex == 'Female':
                femalesenior = femalesenior + 1
            else:
                pendingsenior = pendingsenior + 1
        else:
            pending = pending + 1
            if cust.sex == 'Male':
                malepending = malepending + 1
            elif cust.sex == 'Female':
                femalepending = femalepending + 1
            else:
                pendingunknown = pendingunknown + 1

    # sex_query = request.GET.get('sex')
    # classification_query = request.GET.get('classification')

    # if classification_query != '' and classification_query is not None:
    #     customer = customer.filter(permanent_address__icontains=classification_query)

    context = {
        "maleCount": maleCount,
        "femaleCount": femaleCount,
        "otherCount": otherCount,
        "customer": customer,
        "youngadult": youngadult,
        "adult": adult,
        "senior": senior,
        "pending": pending,
        "maleyoungadult": maleyoungadult,
        "femaleyoungadult": femaleyoungadult,
        "pendingyoungadult": pendingyoungadult,
        "maleadult": maleadult,
        "femaleadult": femaleadult,
        "pendingadult": pendingadult,
        "malesenior": malesenior,
        "femalesenior": femalesenior,
        "pendingsenior": pendingsenior,
        "malepending": malepending,
        "femalepending": femalepending,
        "pendingunknown": pendingunknown
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
    customer = Profile.objects.get(user_id=pk)
    customerUser = User.objects.get(id =pk)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=customerUser)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=customer)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('customersearch')
    else:
        u_form = UserUpdateForm(instance=customerUser)
        p_form = ProfileUpdateForm(instance=customer)
    
    context = {
        "customer": customer,
        "customerUser": customerUser,
        "u_form": u_form,
        "p_form" : p_form
    }

    return render(request, 'markitten_app/update.html', context)

def delete(request, pk):
    customer = Profile.objects.get(id=pk)
    customer.delete()

    return redirect('customersearch')