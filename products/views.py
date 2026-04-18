from django.shortcuts import render

def catalog(request):
    context={
        "title":"Каталог"
    }
    return render(request, 'products/catalog.html',context)
def product(request):
    context={
    "title":"Продукт"
    }
    return render(request, 'products/product.html',context)
