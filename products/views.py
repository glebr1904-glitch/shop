from django.shortcuts import render,get_list_or_404
from django.core.paginator import Paginator
from products.models import Product

def catalog(request,category_slug):
    page=request.GET.get('page',1)
    on_sale=request.GET.get("on_sale", None)
    order_by=request.GET.get("order_by", None)
    if category_slug=="all":
        products=Product.objects.all()
    else:
        products=Product.objects.filter(category__slug=category_slug)

    if on_sale:
        products=products.filter(discounts__gt=0)
    
    if order_by and order_by!="default":
        products=products.order_by(order_by)

    products=get_list_or_404(products)

    paginator=Paginator(products,3)
    current_page=paginator.page(int(page))
    context={
        "title":"Каталог",
        "products": current_page,
        'category_slug':category_slug
    }
    return render(request, 'products/catalog.html',context)
def product(request,product_slug):
    product=Product.objects.get(slug=product_slug)
    context={
    "title":"Продукт",
    "product":product
    }
    return render(request, 'products/product.html',context)
