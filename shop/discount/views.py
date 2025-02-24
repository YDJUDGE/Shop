from django.shortcuts import render
from .models import Discount
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
import random

@login_required
def spin_wheel(request):
    last_discount = Discount.objects.filter(user=request.user).order_by('-created_at').first()

    # Если скидка существует и еще не истекла, то запрашиваем прокрутку
    if last_discount and last_discount.expired_at > now():
        remaining_seconds = (last_discount.expired_at - now()).total_seconds()
        remaining_hours = remaining_seconds // 3600  # Вычисление оставшегося времени в часах
        remaining_minutes = (remaining_seconds % 3600) // 60  # Вычисление оставшегося времени в минутах
        return render(request, "wheel/discount_wheel.html", {
            "error": "You must wait {:.0f} hours. and {:.0f} minutes".format(remaining_hours, remaining_minutes),
            "show_form": False,
            "discount": last_discount,
            "expires_at": last_discount.expired_at.strftime("%Y-%m-%d %H:%M:%S")
        }, status=400)  # Рендеринг оставшего времени скидки и её истечения

    if request.method == "POST":
        # Удаляем старую скидку, если такая была
        Discount.objects.filter(user=request.user).delete()

        # Выдача новой скидки
        discount_values = [5, 10, 15, 20, 25, 29]
        win_chance = [0.5, 0.4, 0.3, 0.2, 0.05, 0.02]
        discount = random.choices(discount_values, weights=win_chance, k=1)[0]  # Берем одно количество случайных элементов

        discount_obj = Discount.objects.create(user=request.user, value=discount, expired_at=now() + timedelta(days=2))

        return render(request, "wheel/discount_wheel.html", {
            'discount': discount,
            'expires_at': discount_obj.expired_at.strftime("%Y-%m-%d %H:%M:%S"),
            "show_form": False
        })

    return render(request, "wheel/discount_wheel.html", {"show_form": True})
