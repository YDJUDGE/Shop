from django.db import models
from django.db.models import Manager

from myauth.models import MyCustomUser
from products.models import Shoes
from typing import TYPE_CHECKING


class Order(models.Model):
    username = models.ForeignKey(MyCustomUser, on_delete=models.PROTECT, null=True, blank=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, help_text="Введите email, на который придёт код подтверждения заказа")
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    if TYPE_CHECKING:
        objects: Manager

    class Meta:
        ordering = ('-created',)  # Сортировка в обратном порядке

    def __str__(self):
        return f"Заказ {self.pk}, Пользователя {self.username}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Shoes, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f"{self.quantity}$ за {self.product.name}"

    def get_cost(self):
        return self.price * self.quantity



