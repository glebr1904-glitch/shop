from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50, unique=True,verbose_name="Наименование")
    slug=models.SlugField(max_length=50, unique=True, blank=True,null=True,verbose_name="URL")
    class Meta:
        db_table="categories"
        verbose_name="Категорию"
        verbose_name_plural="Категории"    
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=50, unique=True,verbose_name="Наименование")
    slug=models.SlugField(max_length=50, unique=True, blank=True,null=True,verbose_name="URL")
    price=models.DecimalField(max_digits=6,decimal_places=2, default=0,verbose_name="Цена")
    sell_price=models.DecimalField(max_digits=6,decimal_places=2, default=0,verbose_name="Цена со скидкой")
    image=models.ImageField(upload_to="image_products",blank=True,null=True,verbose_name="Картинка")
    description=models.TextField(verbose_name="Описание")
    discounts=models.PositiveIntegerField(default=0,verbose_name="Скидка")
    quantity=models.PositiveIntegerField(default=0,verbose_name="Количество")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        db_table="products"
        verbose_name="Продукт"
        verbose_name_plural="Продукты"
        ordering=("id",)
    def __str__(self):
        return f"Название: {self.name} | Цена: {self.price} | Количество: {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"
    
    def save(self, *args, **kwargs):
        self.sell_price=round(self.price-self.price*self.discounts/100,2)
        super().save(*args,**kwargs)
