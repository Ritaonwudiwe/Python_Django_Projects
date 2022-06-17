from django.urls import path
from .views import blog, about, contact, services, booking

app_name = "blog"

urlpatterns = [
    path("", blog, name = "homeView"),
    path("aboutpage/", about, name = "aboutView"),
    path("contactpage/", contact, name = "contactView"),
    path("servicespage/", services, name = "servicesView"),
    path("bookingpage/", booking, name = "bookingView"),
]