from django.shortcuts import render

from store.models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    context={
             "categories": categories,
             "products": products,}
    return render(request, "index.html",context)

def admin_panel(request):
    return render(request, "admin.html")

def shop(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, "shop.html",  {"categories": categories})

def cart(request):
    return render(request, "cart.html")

def bestseller(request):
    return render(request, "bestseller.html")

def single(request):
    return render(request, "single.html")

def shop_detail(request):
    return render(request, "shop-detail.html")

def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

def er404(request):
    return render(request, "404.html")

