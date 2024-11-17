from django.contrib import admin
from .models import User, CartItem, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")

    search_fields = ("id",)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product_name", "quantity", "price")

    search_fields = ("id",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at", "updated_at")

    search_fields = ("id",)
