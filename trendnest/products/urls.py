from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('men/', views.men_products, name='men_products'),
    path('category/women/', views.women_products, name='women-products'),
    path('kids/', views.kids_products, name='kids_products'),
    path('category/<slug:category_slug>/', views.category_view, name='category_view'),
]
