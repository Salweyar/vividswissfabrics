from django.shortcuts import render
from django.http import HttpResponse
from .models import newCollection
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    obj = newCollection.objects.get(id=1)
    obj_2 = newCollection.objects.get(id=2)
    obj_3 = newCollection.objects.get(id=3)
    obj_4 = newCollection.objects.get(id=4)
    context = {
        'object': obj,
        'object_2': obj_2,
        'object_3': obj_3,
        'object_4': obj_4
    }
    return render(request, "home.html", context)

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