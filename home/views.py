from django.shortcuts import render
from products.models import Category, Product
from django.shortcuts import render, redirect

def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_available=True)[:8]
    return render(request, 'home.html', {
        'categories': categories,
        'featured_products': featured_products,
    })
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # or redirect to any page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

