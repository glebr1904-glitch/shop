from django.shortcuts import render


def index(request):
    context={
        "title":"Главная страница",
        "header":"Магазин компьютерных игр Game zona",
        # "games":[
            # {'title':'Mainckraft','price':'349', 'amount':'930'},
            # {'title':'PUBG','price':'349', 'amount':'1030'},
            # {'title':'CS2','price':'349', 'amount':'130'},
            # {'title':'Dota2','price':'199', 'amount':'30'},
            # {'title':'CS 1.6','price':'549', 'amount':'150'},
        # ],
        # "genres":["Шутеры","RPG","Симулятор"]
    }
    return render(request,'main/index.html', context)

def about(request):
    context={
        'title':'О нас',
        'about':'Мы Game Zone. Мы зaнимаемся продажей компютерных игр.'
    }
    return render (request,'main/about.html',context)






