from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.models import Cart, CartItem

def order_create(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.username = request.user  # Связываем заказ и пользователя
            total_price = 0
            order.save()
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
                total_price += item.product.price * item.quantity
            order.total_price = total_price
            order.save(update_fields=["total_price"])
            cart.delete()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})

def order_list(request):
    all_orders = Order.objects.filter(username_id=request.user.id).order_by('-created')
    return render(request, "orders/orders_by_user.html", context={"all_orders": all_orders})

