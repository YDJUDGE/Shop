from django.db import models
from myauth.models import MyCustomUser
import uuid
from django.utils.timezone import now, timedelta
from django.db.models import Manager
from typing import TYPE_CHECKING


class Discount(models.Model):
    user = models.OneToOneField(MyCustomUser, on_delete=models.PROTECT)
    value = models.PositiveIntegerField()  # это скидка
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    if TYPE_CHECKING:
        objects: Manager

    def save(self, *args, **kwargs):
        if not self.expired_at:
            self.expired_at = now() + timedelta(days=2)
        super().save(*args, **kwargs)

    def is_active(self):
        return not self.used and self.expired_at > now()

