from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "templates/frontend/pages/home/home.html")

def sell(request):
    return render(request, "templates/frontend/pages/sell/sell.html")

def aboutus(request):
    return render(request, "templates/frontend/pages/aboutus/aboutus.html")
