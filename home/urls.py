from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path("", home),
    path("aboutpage/", about),
    path("contactpage/", contact),
]
