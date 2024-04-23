from django.contrib import admin
from .models import Category,Product,Order

# Register your models here.

# The `@admin.register(Category)` decorator is used in Django to register a model with the Django
# admin interface. In this case, the `Category` model is being registered with the Django admin
# interface, which allows you to manage and interact with instances of the `Category` model through
# the admin panel. By using this decorator, you can customize how the model is displayed and
# interacted with in the admin interface by defining a custom `ModelAdmin` class.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','description','created_at','updated_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','description','price','image','category','created_at','updated_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email','product','quantity','created_at','updated_at']
