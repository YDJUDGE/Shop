from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, update_cart

app_name = "cart"

urlpatterns = [
    path("cart/", cart_view, name="cart_view"),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path("update/<int:item_id>/", update_cart, name="update_cart")
]
