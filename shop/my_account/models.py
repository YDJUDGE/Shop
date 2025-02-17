from typing import TYPE_CHECKING
from django.db import models
from django.db.models import Manager
from myauth.models import MyCustomUser

class Profile(models.Model):
    user = models.OneToOneField(MyCustomUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, help_text="Напишите немного о себе, в будущем это поможет нам предлагать вам уникальные товары и акции")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/", default="profile/user_image.jpg")
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    vk = models.URLField(null=True, blank=True, verbose_name="VK Профиль", help_text="Оставьте ссылку на ваш Вк")  # Данное отображение(имя), будет использованно в админке
    twitter = models.URLField(null=True, blank=True, verbose_name="X Профиль", help_text="Оставьте ссылку на ваш Твиттер")

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return (f"Пользователь: {self.user.name}, id: {self.user.primary_key}")

