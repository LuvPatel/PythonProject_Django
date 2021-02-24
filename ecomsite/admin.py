from django.contrib import admin
from .models.Product import Product
from .models.categories import Category
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['Name','price','fk']
class AdminCategory(admin.ModelAdmin):
    list_display=['Name']
    
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)