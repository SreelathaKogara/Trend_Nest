from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product  # adjust import if your product model is elsewhere
from .models import CartItem
from django.contrib import messages


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []

    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            item_total = product.price * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
        except Product.DoesNotExist:
            continue

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def add_to_cart(request):
    if request.method == "POST":
        product_id = str(request.POST.get("product_id"))
        product = get_object_or_404(Product, id=product_id)

        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('cart:cart_view')  # replace with your actual cart view name

def remove_from_cart(request, product_id):
    item = CartItem.objects.filter(product_id=product_id).first()
    if item:
        item.delete()
    return redirect('cart:cart')
def ordernow(request):
    # This can come from POST/session/cart logic
    product_name = request.POST.get('product_name', 'Floral Kurta Set')
    product_price = request.POST.get('product_price', '1200')
    brand_name = request.POST.get('brand_name', 'Zara')

    return render(request, 'ordernow.html', {
        'product_name': product_name,
        'product_price': product_price,
        'brand_name': brand_name,
    })
def checkout(request):
    return render(request, 'cart/checkout.html')