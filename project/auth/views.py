from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Auth App Home Page!")

def login(request):
    return HttpResponse("Login Page")
def logout(request):
    return HttpResponse("Logout Page")

