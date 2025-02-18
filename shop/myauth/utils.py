import random
from django.core.mail import send_mail
from django.conf import settings

def generate_special_code():
    """Генерирует случайный код из 6 чисел"""
    return str(random.randint(100000, 999999))

def send_verification_email(request, user):
    """Отправляет код на email юзера"""
    code = generate_special_code()
    user.verification_code = code  # Сохранение кода в БД
    user.save()

    request.session["verification_code"] = code

    print(f"Отправка email {user.email} с кодом {code}")

    send_mail(
        "Код подтверждения",
        f"Ваш код подтверждения: {code}",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False  # Что это?
    )
