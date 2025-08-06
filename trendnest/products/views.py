from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    search_query = request.GET.get('q')

    # Search filter
    if search_query:
        products = products.filter(name__icontains=search_query)

    if selected_category:
        selected_category = selected_category.strip()  # <-- Extra tip: strip spaces to avoid lookup issues
        try:
            category_obj = Category.objects.get(category_name__iexact=selected_category)
            products = products.filter(category=category_obj)
        except Category.DoesNotExist:
            products = Product.objects.none()

    # Price sort
    price_order = request.GET.get("price")
    if price_order == "low_to_high":
        products = products.order_by("price")
    elif price_order == "high_to_low":
        products = products.order_by("-price")

    # Calculate discount percentage for each product
    for product in products:
        if product.original_price and product.original_price > product.price:
            discount = ((product.original_price - product.price) / product.original_price) * 100
            product.discount_percentage = int(discount)
        else:
            product.discount_percentage = 0

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def login_view(request):
    return render(request, 'login.html')


def men_products(request):
    products = Product.objects.filter(category__category_name__iexact='Men')

    for product in products:
        if product.original_price and product.original_price > product.price:
            product.discount_percentage = int(((product.original_price - product.price) / product.original_price) * 100)
        else:
            product.discount_percentage = 0

    return render(request, 'products/men.html', {'products': products})

def women_products(request):
    products = Product.objects.filter(category__category_name__iexact='Women')

    for product in products:
        if product.original_price and product.original_price > product.price:
            product.discount_percentage = int(((product.original_price - product.price) / product.original_price) * 100)
        else:
            product.discount_percentage = 0

    return render(request, 'products/women.html', {'products': products})



def kids_products(request):
    products = Product.objects.filter(category__category_name__iexact='Kids')

    for product in products:
        if product.original_price and product.original_price > product.price:
            product.discount_percentage = int(((product.original_price - product.price) / product.original_price) * 100)
        else:
            product.discount_percentage = 0

    return render(request, 'products/kids.html', {'products': products})

def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }

    # Choose the template based on category slug
    if category.slug == 'men':
        template_name = 'men.html'
    elif category.slug == 'women':
        template_name = 'women.html'
    elif category.slug == 'kids':
        template_name = 'kids.html'
    else:
        template_name = 'products_by_category.html'  # fallback


    return render(request, f'products/{template_name}', context)
def cart_view(request):
    return render(request, 'trendnest/cart/cart.html')