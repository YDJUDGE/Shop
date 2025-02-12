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
            order.user = request.user
            order.save()
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
                cart.clean()
                return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


