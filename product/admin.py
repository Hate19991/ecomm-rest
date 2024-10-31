from django.contrib import admin
from .models import Category, Brand, ProductImage, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    # list_per_page = 20
    ...
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

class BrandAdmin(admin.ModelAdmin):
    list_display = ["id","name","profile_image"]
                    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
