from django.shortcuts import render, get_object_or_404, redirect
from products.models import Shoes
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required  # Использую, чтобы только авторизованные пользователи, могли делать действия с товарами
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart.html", {"cart": cart})  # Это конструкция для корректной передачи корзины в шаблон

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Shoes, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
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
