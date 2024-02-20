"""Smaugefashionhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.LandingPage),
    path("about.html/", views.AboutUs),
    path("blog.html/", views.Blog),
    path("contact.html/", views.Contact),
    path("policy.html/", views.Policy),
    path("login.html/", views.Login),
    path("signin.html/", views.Signin),
    path("faq.html/", views.faq),
    path("products.html/", views.Products),
    path("login.html/signup.html/", views.Signup),
] 
