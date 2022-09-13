from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from datetime import date
import secrets


# Create your views here.

def welcome(request):
    return render(request, "lab3app/base.html")
    

def day(request):
    today = date.today()
    return render(request, "lab3app/index.html", {"today":today})

def book(request):
    books = ["Start with why","The First 90 days", "Execution"]
    return render(request, "lab3app/book.html", {"books":books})


def pas_w(request):
    password_length = 14
    return render(request ,"lab3app/pass.html",{"pass": secrets.token_urlsafe(password_length)}) 

    
def contact(request):
    email = "realalharbi3@gmail.com"
    return render(request , "lab3app/contact.html",{"email": email})


