from django.shortcuts import render
from products.models import Product

def catalog(request):
    products=Product.objects.all()
    context={
        "title":"Каталог",
        "products":products,
    }
    return render(request, 'products/catalog.html',context)
def product(request):
    context={
    "title":"Продукт"
    }
    return render(request, 'products/product.html',context)
