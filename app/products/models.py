from django.db import models
from users.models import Users


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)  # уникальный
    description = models.TextField(blank=True)  # необязательное заполнение

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='users image', blank=True)
    description = models.TextField(blank=True)
    s_description = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=(("Не оплачено", "no paid"), ("Оплачено", "paid")), default='no paid', max_length=15)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина {self.user.username}| Продукт {self.product.name}'

    def sum(self):
        return self.count * self.product.price

    def paid(self):
        self.status = 'paid'


class Exchanges(models.Model):
    usd = models.FloatField()
    eur = models.FloatField()

    def __str__(self):
        return "Курс валют"
