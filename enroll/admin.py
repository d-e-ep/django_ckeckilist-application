from django.contrib import admin
from .models import user
# Register your models here.
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name' , 'email' , 'mobile_no' , 'password' )