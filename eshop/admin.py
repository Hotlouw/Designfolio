from django.contrib import admin
from .models import Product, Category, Supplier, CartItem
from .models import UserProfile

admin.site.register(UserProfile)



admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(CartItem)