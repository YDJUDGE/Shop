from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class MyCustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True, default="")

UserModel: AbstractUser = get_user_model()

