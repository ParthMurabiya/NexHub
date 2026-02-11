from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    return render(request, "register.html")

def login(request):
    if request.session.get("user_id"):
        return redirect("store:index")
    return render(request, "login.html")

def logout(request):
    request.session.flush()   
    return redirect("login:login")

def create_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]

        hashed_password = make_password(password) 

        Account.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            password=hashed_password
        )
        return redirect("login:login")

    return redirect("login:register")
    
def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = Account.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            request.session["user_id"] = user.id  # store login
            return redirect("store:index")

        return redirect("login:login")

def profile(request):
    if not request.session.get("user_id"):
        return redirect("login:login")
    return render(request, "profile.html")