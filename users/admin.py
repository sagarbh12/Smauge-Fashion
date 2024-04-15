from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'contact_number','is_verified')

    exclude=['password','email_token']
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
