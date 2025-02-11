from django.db import models
from typing import TYPE_CHECKING
from django.db.models import Manager


class Shoes(models.Model):
    class Meta:
        pass
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products_images/", blank=True)

    if TYPE_CHECKING:
        objects: Manager

    def  __str__(self):
        return f"{self.name} - {self.price}$"
