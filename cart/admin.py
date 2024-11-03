from django.contrib import admin
from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_added']
    
class CartItemAdmin(admin.ModelAdmin):  
      list_display = ['id','cart', 'product' , 'quantity', 'date_added']
      search_fields = ['id', 'user', 'date_added']
      
admin.site.register(Cart , CartAdmin)
admin.site.register(CartItem , CartItemAdmin)