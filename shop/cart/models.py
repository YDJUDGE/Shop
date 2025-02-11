from django.db import models
from myauth.models import MyCustomUser
from products.models import Shoes


class Cart(models.Model):
    user = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Даю возможнсть пользователю управлять количеством товара в корзине

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

