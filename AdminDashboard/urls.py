from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
<<<<<<< HEAD
    path("adminn/", views.Adminn, name ='adminn'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('allorders/', views.Allorders, name='allorders'),
    path('allproducts/', views.Allproducts, name='allproducts'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('allusers/', views.Allusers, name='allusers'),
    path('settings/', views.Settings, name='settings'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

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
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154
