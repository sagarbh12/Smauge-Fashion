import uuid
from django.contrib import admin
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .utils import *
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from google.oauth2 import id_token
from google.auth.transport import requests
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from AdminDashboard.models import productsModel
=======
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154


def LandingPage(request):
    data={
        'Title': 'Smauge Fashion Hub'
    }
    return render(request, 'users/index.html', data)  # data jun chai HTML page maa dekhauna chahancha....

def AboutUs(request):
    return render(request, "users/about.html")

def Blog(request):
    return render(request, "users/blog.html")

def Contact(request):
    return render(request, "users/contact.html")

<<<<<<< HEAD
def Refund(request):
=======
def RefundPolicy(request):
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154
    return render(request, "users/RefundPolicy.html")

def PrivacyPolicy(request):
    return render(request, "users/PrivacyPolicy.html")

def faq(request):
    return render(request, "users/faq.html")

def Products(request):
<<<<<<< HEAD
    # Fetch all existing products from the database
    products = productsModel.objects.all()
    return render(request, "users/products.html",{'products': products})
    return render(request, "users/products.html")

def Testimonial(request):
    return render(request, "users/testimonial.html")

=======
    return render(request, "users/products.html")

>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154

def Signup(request):
    context = {
                'username': '',
                'fullname': '',
                'email': '',
                'contact': '',
                'pass1': '',
                'pass2': '',
            }
    if request.method == 'POST':
        username= request.POST['username'] # accesed from the name in the form
        fullname= request.POST['fullname']
        email= request.POST['email']
        contact= request.POST['contact'] 
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        context = {
                'username': username,
                'fullname': fullname,
                'email': email,
                'contact': contact,
                'pass1': pass1,
                'pass2': pass2,
            }
        status=False
        if CustomUser.objects.filter(username=username):
            status=True
            messages.error(request, "Username is already in use. Please choose a different username.")
      
        if CustomUser.objects.filter(email=email):
            status=True
            messages.error(request, "Email address is already in use. Please use a different email.")
        
        if len(username) > 15:
            status=True
            messages.error(request, "The username cannot be longer than 15 characters.")

        if pass1!=pass2:
             status=True
             messages.error(request, "The passwords don't match.")

        alphanumeric_pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

        # Check if username contains only alphanumeric characters
        if not alphanumeric_pattern.match(username):
            status = True
            
            messages.error(request, "The username must be alphanumeric and contain atleast 8 characters.")

       

        # Check if password contains only alphanumeric characters
        if not alphanumeric_pattern.match(pass1):
            status = True
            messages.error(request, "The password must be alphanumeric and contain atleast 8 characters.")

        if CustomUser.objects.filter(contact_number=contact):    
            status=True
            messages.error(request, "The contact number is already in use. Please choose a different contact number.")
           
        if len(str(contact)) !=10:
            status=True
            print("hello")
            messages.error(request, "The contact number should be exactly 10 digits" )

        if status:
          return render(request, 'users/signup.html',context)
           
        email_token = str(uuid.uuid4())
        my_user=CustomUser.objects.create_user(username,email,pass1)
        my_user.full_name=fullname
        my_user.contact_number=contact
        my_user.email_token = email_token
        my_user.save()
        send_email_token(email,email_token)
        messages.success(request, "Your account was successfully created. Please check your email for verification.")
        return redirect('login')
        

    return render(request, 'users/signup.html',context)


def Login(request):
<<<<<<< HEAD
    context = {'username': ''}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']  # Corrected the variable name from pass1 to password

        context = {'username': username}
        print('chor')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_verified:  # Check if user is verified
            login(request, user)
            if user.is_superuser:  # Check if user is an admin
                messages.success(request, "Admin login successful!")
                return redirect('adminn')  # Redirect to admin page
            else:
                fullname = user.full_name
                messages.success(request, "Successfully logged in!")
                return redirect("index")
        elif user is not None and not user.is_verified:
            messages.error(request, "Your email is not verified yet. Please check your email for verification.")
            
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html', context)
=======
    context={ 'username':''

    }
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']

        context={ 'username':username

            }

        user= authenticate(username=username, password=pass1)
        if user is not None and user.is_verified:  # Check if user is verified
            login(request, user)
            fullname = user.full_name
            messages.success(request, "Successfully logged in!")
            return render(request, 'users/index.html', {'fullname': fullname})
        elif user is not None and not user.is_verified:
            messages.error(request, "Your email is not verified yet. Please check your email for verification.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html',context)

>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154


def VerifyEmail(request, token):
    try:
        user = CustomUser.objects.get(email_token=token)
        user.is_verified = True
        user.save()
        messages.success(request, "Your email has been verified. You can now log in.")
    except CustomUser.DoesNotExist:
        messages.error(request, "Invalid verification token.")

    return redirect('login')

def ForgotPassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = CustomUser.objects.get(username=username)
            email= user.email

            # Generate a unique token for password reset
            password_token = str(uuid.uuid4())
            user.password_reset_token = password_token
            user.save()
            send_password_token(email,password_token)

        
            messages.success(request, "Password reset link has been sent to your email.")
            return redirect('forgot_password')

        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('forgot_password')

    return render(request, 'users/forgot-password.html')


def ResetPassword(request, token):
   
    try:
        user = CustomUser.objects.get(password_reset_token=token)
        
        if request.method == 'POST':
            new_password = request.POST.get('new-password')
            confirm_password = request.POST.get('confirm-password')
           

            if new_password != confirm_password:
                messages.error(request, "Passwords don't match")
                return redirect(f'/reset-password/{token}/')
            
            alphanumeric_pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

            if not alphanumeric_pattern.match(new_password):
                messages.error(request, "The password must be alphanumeric and contain atleast 8 characters.")
                return redirect(f'/reset-password/{token}/')
            
         
            user.set_password(new_password)
            user.save()
            messages.success(request,"Your password was reset successfully!")
            return redirect('login')

    except CustomUser.DoesNotExist:
        messages.error(request, "Invalid password reset token")
        return redirect('forgot_password')

    return render(request, 'users/reset-password.html')



@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), '803641603998-mtkrdl2sq8797su0okkm6v96epn5eo65.apps.googleusercontent.com'
        )
        print(user_data)
        
        
    except ValueError:
        return HttpResponse(status=403)

    
    try:
        user = CustomUser.objects.get(email=user_data['email'])
        # Log in the user
        login(request, user)

        # Redirect to dashboard if user exists
        return redirect('index')
    except CustomUser.DoesNotExist:
        
        user = CustomUser.objects.create_user(
            username=user_data['email'],  
            email=user_data['email'],
            full_name=user_data.get('name', ''),
            is_verified=True
        )

    # Log in the user
    login(request, user)
    return redirect('inputcontact')


def inputcontact(request):
    if request.method == 'POST':
        contact = request.POST.get('contact_number')
        status=False
        if CustomUser.objects.filter(contact_number=contact):    
          status=True
          messages.error(request, "The contact number is already in use. Please choose a different contact number.")
        
        if len(str(contact)) !=10:
            status=True
     
            messages.error(request, "The contact number should be exactly 10 digits" )

        if status:
            return render(request, 'users/inputcontact.html')

        request.user.contact_number = contact
        request.user.save()
        messages.success(request, "login successful")
        return redirect('index')  
    
    return render(request, 'users/inputcontact.html')
