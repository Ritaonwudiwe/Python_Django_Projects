from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signuppage/", signup, name="signupView"),
    path("loginpage/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="loginView"),
    path("logoutpage/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logoutView"),
]
