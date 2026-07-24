from django.shortcuts import render
from products.models import Category,Product

def index(request):
    categories=Category.objects.all()
    context={
        
        "title":"Главная страница",
        "header":"Магазин световодиодное оборудование DREAM ",
        "categories":categories,

    }
    return render(request,'main/index.html', context)

def about(request):
    context={
        'title':'О нас',
        'about':'Мы Game Zone. Мы зaнимаемся продажей компютерных игр.'
    }
    return render (request,'main/about.html',context)






