# Generated by Django 5.1.5 on 2025-02-14 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        help_text="Напишите немного о себе, в будущем это поможет нам предлагать вам уникальные товары и акции",
                        null=True,
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                (
                    "vk",
                    models.URLField(
                        blank=True,
                        help_text="Оставьте ссылку на ваш Вк",
                        null=True,
                        verbose_name="VK Профиль",
                    ),
                ),
                (
                    "twitter",
                    models.URLField(
                        blank=True,
                        help_text="Оставьте ссылку на ваш Твиттер",
                        null=True,
                        verbose_name="X Профиль",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
