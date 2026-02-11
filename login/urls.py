from django.urls import path
from login import views

app_name = "login"   # ⭐ important

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("create/", views.create_user, name="create"),
    path("login-user/", views.login_user, name="login_user"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
   

]
