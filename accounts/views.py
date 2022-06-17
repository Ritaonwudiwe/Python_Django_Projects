from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def signup(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect("blog:homeView")
        else:
            return redirect("accounts:loginView")    
    context = {
        "form":UserCreationForm(),
    }
    return render(request, 'accounts/django-register.html', context)
    
    
#def login(request):
    #return render(request, 'accounts/login.html')