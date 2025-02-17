from django.urls import path
from .views import order_create, order_list

app_name = "order"

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('list_orders/', order_list, name='list_orders'),
]

