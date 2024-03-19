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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [

    path("", views.LandingPage, name='index'),
    path("about/", views.AboutUs),
    path("blog/", views.Blog),
    path("contact/", views.Contact),
    path("RefundPolicy/", views.RefundPolicy),
    path("PrivacyPolicy/", views.PrivacyPolicy),
    path("faq/", views.faq),
    path("products/", views.Products),
    path("login/", views.Login, name ='login'),
    # path('logout', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path("signup/", views.Signup, name='signup'),
    path('verify/<str:token>/',views.VerifyEmail,name='verify_email'),
    path('forgot-password/',views.ForgotPassword,name='forgot_password'),
    path('reset-password/<str:token>/',views.ResetPassword,name='reset_password'),
    path('inputcontact/',views.inputcontact, name='inputcontact'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
] 
