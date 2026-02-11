from django.urls import path
from store import views

app_name = "store"   # ⭐ important

urlpatterns = [
    path("", views.index, name="index"),
    path("admin-panel/", views.admin_panel, name="admin-panel"),
    path("shop/", views.shop, name="shop"),
    path("shop-detail/", views.shop_detail, name="shop_detail"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("contact/", views.contact, name="contact"),
    path("404/", views.er404, name="404"),
    path("bestseller/", views.bestseller, name="bestseller"),
    path("single/", views.single, name="single"),
    

]
