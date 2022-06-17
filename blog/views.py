from django.shortcuts import render
from django.shortcuts import redirect, render
from blog.models import customer_detail
#from django.contrib.auth.models import user
#from django.contrib.auth import authenticate, login


# Create your views here.
def blog(request):
    return render(request, 'hotel/index.html')
    
def about(request):
    return render(request, 'hotel/about.html')
    
def contact(request):
    return render(request, 'hotel/contact.html')

def services(request):
    return render(request, 'hotel/services.html')

def booking(request):
    if request.method == "POST":
        occ_n = request.POST.get("occ_n")
        occ_e = request.POST.get("occ_e")
        occ_o = request.POST.get("occ_o")
        room_num = request.POST.get("room_num")
        amount = request.POST.get("amount")
        no_of_night = request.POST.get("no_of_night")
        start_date = request.POST.get("start_date")
        end_date= request.POST.get("end_date")

        new_booking = customer_detail(occupant_name=occ_n, occupant_email=occ_e, occupant_occupation=occ_o, room_number=room_num, amount_paid=amount, number_of_night=no_of_night, start_date=start_date, end_date=end_date)
        new_booking .save()
        return redirect("blog:homeView")
    return render(request, 'hotel/booking.html')   

