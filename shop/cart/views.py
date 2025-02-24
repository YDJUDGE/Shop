from decimal import Decimal

from django.shortcuts import render, get_object_or_404, redirect
from products.models import Shoes
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from discount.models import Discount
from django.utils.timezone import now

@login_required  # Использую, чтобы только авторизованные пользователи, могли делать действия с товарами
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart.html", {"cart": cart})  # Это конструкция для корректной передачи корзины в шаблон

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Shoes, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    user_discount = None
    if request.user.is_authenticated:
        user_discount = Discount.objects.filter(user=request.user, expired_at__gte=now(), used=False).first()

    discount = Decimal(user_discount.value) if user_discount else Decimal(0)
    discounted_price = round(product.price * (Decimal(1) - discount / Decimal(100)), 2)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        cart_item.price = discounted_price
    else:
        cart_item.quantity += 1

    cart_item.price = discounted_price
    cart_item.save()

    return redirect("cart:cart_view")

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)  # cart__user - это обращение к связанному объекту (Django ORM)
    cart_item.delete()
    return redirect("cart:cart_view")

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart:cart_view")
