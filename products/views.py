from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    search_query = request.GET.get('q')

    if selected_category:
        products = products.filter(category__name=selected_category)

    if search_query:
        products = products.filter(name__icontains=search_query)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories
    })
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
def login_view(request):
    return render(request, 'login.html')