from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class MyCustomUser(AbstractUser):
    pass

UserModel: AbstractUser = get_user_model()

