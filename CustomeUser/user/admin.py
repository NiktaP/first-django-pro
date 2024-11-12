from django.contrib import admin
from .models import CustomUser
# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','password']
    fields = ['email','first_name','last_name','password','date_joined','user_name','phone_number',('is_staff','is_active')]


admin.site.register(CustomUser, Useradmin)