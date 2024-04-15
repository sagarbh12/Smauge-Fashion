import uuid
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from users.models import CustomUser
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from .models import productsModel
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


def Adminn(request):
    return render(request, 'adminn.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def logout(request):
    return render(request, 'index.html')


def Allproducts(request):
    if request.method == 'POST':
        name = request.POST.get('Jacket_Name')
        description = request.POST.get('Description')
        image = request.FILES.get('Image')
        price = request.POST.get('Price')
        
        if name and description and image and price:
            # Save data to the database
            productsModel.objects.create(Jacket_Name=name, Description=description, Image=image, Price=price)
            messages.success(request, "Successfully Added!")
            return redirect('allproducts')  # Redirect to the same page after form submission
        else:
            messages.error(request, "All fields are required.")
    
    # Fetch all existing products from the database
    products = productsModel.objects.all()
    
    return render(request, 'allproducts.html', {'products': products})


def edit_product(request, product_id):
    product = productsModel.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.Jacket_Name = request.POST.get('Jacket_Name')
        product.Description = request.POST.get('Description')
        product.Price = request.POST.get('Price')
        
        # Check if a new image file was uploaded
        image = request.FILES.get('Image')
        if image:
            product.Image = image
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('allproducts')
    # Fetch all products from the database
    products = productsModel.objects.all()
    
    # Render the edit product page with the product details and all products
    return render(request, 'edit_product.html', {'product': product, 'products': products})


def delete_product(request, product_id):
    if request.method == 'POST':
        try:
            # Retrieve the product from the database
            product = productsModel.objects.get(id=product_id)
            # Delete the product from the database
            product.delete()
            # Return success response
            return JsonResponse({'success': True})
        except productsModel.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product does not exist'}, status=404)
    else:
        # Return error response if request method is not POST
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


def Allorders(request):
    # if request.method == 'POST':
    #     name = request.POST.get('Jacket_Name')
    #     description = request.POST.get('Description')
    #     image = request.FILES.get('Image')
    #     price = request.POST.get('Price')
        
        
    #     # Save data to the database
    #     productsModel.objects.create(Jacket_Name=name, Description=description, Image=image, Price=price)
        
    #     messages.success(request, "Successfully Added!")
    return render(request, 'allorders.html')

def Allusers(request):
    if request.method == 'POST':
        name = request.POST.get('Jacket_Name')
        description = request.POST.get('Description')
        image = request.FILES.get('Image')
        price = request.POST.get('Price')
        
        if name and description and image and price:
            # Save data to the database
            productsModel.objects.create(Jacket_Name=name, Description=description, Image=image, Price=price)
            messages.success(request, "Successfully Added!")
            return redirect('allproducts')  # Redirect to the same page after form submission
        else:
            messages.error(request, "All fields are required.")
    
    # Fetch all existing products from the database
    products = productsModel.objects.all()
    
    return render(request, 'allproducts.html', {'products': products})


def Settings(request):
    # if request.method == 'POST':
    #     name = request.POST.get('Jacket_Name')
    #     description = request.POST.get('Description')
    #     image = request.FILES.get('Image')
    #     price = request.POST.get('Price')
        
   
    #     # Save data to the database
    #     productsModel.objects.create(Jacket_Name=name, Description=description, Image=image, Price=price)
        
    return render(request, 'settings.html')
=======
import re


def AdminDashboard(request):
    return render(request, 'adminn.html') 

def AboutUs(request):
    return render(request, "users/about.html")

def Blog(request):
    return render(request, "users/blog.html")

def Contact(request):
    return render(request, "users/contact.html")

def RefundPolicy(request):
    return render(request, "users/RefundPolicy.html")

def PrivacyPolicy(request):
    return render(request, "users/PrivacyPolicy.html")

def faq(request):
    return render(request, "users/faq.html")

def Products(request):
    return render(request, "users/products.html")


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
            return render(request, 'users/index.html', {'fullname': fullname})
        elif user is not None and not user.is_verified:
            messages.error(request, "Your email is not verified yet. Please check your email for verification.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html',context)


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
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154
