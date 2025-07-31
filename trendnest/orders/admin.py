from django.contrib import admin
from .models import Coupon, Cart, CartItem, Order, OrderItem

admin.site.register(Coupon)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
