from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/index.html')
    #return HttpResponse("<h1> home page </h1>")

def about(request):
    return render(request, 'home/about.html')
    #return HttpResponse("<h1> about page </h1>")

def contact(request):
    return render(request, 'home/contact.html')
    #return HttpResponse("<h1> contact page </h1>")
