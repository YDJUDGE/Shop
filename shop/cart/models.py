from django.db import models
from myauth.models import MyCustomUser
from products.models import Shoes
from typing import TYPE_CHECKING
from django.db.models.manager import Manager


class Cart(models.Model):
    user = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    if TYPE_CHECKING:
        objects: Manager  # Нужно, чтобы мы могли обращатся как к объекту (без явного объявления object)

    def __str__(self):
        return f"Cart of {self.user.name}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Даю возможнсть пользователю управлять количеством товара в корзине
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def total_price(self):
        return self.price * self.quantity

