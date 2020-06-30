from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "home.html", {})

def contact_us_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "contact_us.html", {})

def services_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "services.html", {})

def shop_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "shop.html", {})

def about_us_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "about_us.html", {})