from django.contrib import admin
<<<<<<< HEAD
from .models import productsModel

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ('Jacket_Name', 'Description', 'display_image', 'Price')

    def display_image(self, obj):
        return '<img src="{}" width="100" />'.format(obj.Image.url)

    display_image.allow_tags = True
    display_image.short_description = 'Image'

# Register the productsModel class with the custom admin class
admin.site.register(productsModel, ProductsModelAdmin)

=======

# Register your models here.
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154
