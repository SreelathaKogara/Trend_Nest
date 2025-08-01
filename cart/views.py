from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product  # adjust import if your product model is elsewhere
from .models import CartItem

def cart_view(request):
    # In real apps, you'd pull cart items from session or DB
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # You can enhance this logic to handle user sessions, quantities, etc.
    CartItem.objects.create(product=product)

    return redirect('product_list')  # redirect to your products list view


def remove_from_cart(request, product_id):
    item = CartItem.objects.filter(product_id=product_id).first()
    if item:
        item.delete()
    return redirect('view_cart')  # Or wherever your cart page is