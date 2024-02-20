from django.http import HttpResponse
from django.shortcuts import render, redirect

# def AboutUs(request):
#     return HttpResponse("Smauge Fashion Hub")


def LandingPage(request):
    data={
        'Title': 'Smauge Fashion Hub'
    }
    return render(request, 'index.html', data)  # data jun chai HTML page maa dekhauna chahancha....

def AboutUs(request):
    return render(request, "about.html")

def Blog(request):
    return render(request, "blog.html")

def Contact(request):
    return render(request, "contact.html")

def Policy(request):
    return render(request, "policy.html")

def Signin(request):
    return render(request, "signin.html")

def Login(request):
    return render(request, "login.html")

def faq(request):
    return render(request, "faq.html")

def Products(request):
    return render(request, "products.html")

def Signup(request):
    return render(request, "signup.html")