from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [

    path("AdminDashboard/", views.AdminDashboard),
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
] 
