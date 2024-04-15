import uuid
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from users.models import CustomUser
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