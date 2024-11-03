from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone_number']
    search_list = ['phone_number']

admin.site.register(Customer, CustomerAdmin)
# Register your models here.