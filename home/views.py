from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Welcome to Home Page </h1>")
    return render(request, "home.html", {})