from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Shoes
from discount.models import Discount
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import ProductCreateForm
from decimal import Decimal

class ListProducts(ListView):
    queryset = Shoes.objects.all()
    template_name = "products/shoe_list.html"
    context_object_name = "shoes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_discount = None
        if self.request.user.is_authenticated:
            user_discount = Discount.objects.filter(
                user=self.request.user, expired_at__gte=now(), used=False
            ).first()  # Пояснения для gte - great than or equal (Больше или равно), здесь мы выбираем ПОСЛЕДНЮЮ скидку, которую получил пользователь

        discount = user_discount.value if user_discount else 0

        # Цены со скидкой
        shoes_with_discount = []
        for shoe in context['shoes']:
            discount_decimal = Decimal(discount) / Decimal('100')
            discount_price = shoe.price * (1 - discount_decimal)
            shoes_with_discount.append({"product": shoe, "discounted_price": round(discount_price, 2)})

        context['shoes'] = shoes_with_discount
        context['discount'] = discount  # Размер скидки в шаблон
        return context

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Shoes
    form_class = ProductCreateForm
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("products:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_discount = None
        if self.request.user.is_authenticated:
            user_discount = Discount.objects.filter(
                user=self.request.user, expired_at__gte=now(), used=False
            ).first()

        discount = user_discount.value() if user_discount else 0
        discount_decimal = Decimal(discount) / Decimal('100')

        context['discount'] = discount
        context["discounted_price"] = round(self.object.price * (1 - discount_decimal), 2)

        return context

    def test_func(self):
        return self.request.user.is_staff

class ProductDetailView(DetailView):
    model = Shoes

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = self.get_object()

        user_discount = None
        if self.request.user.is_authenticated:
            user_discount = Discount.objects.filter(
                user=self.request.user, expired_at__gte=now(), used=False
            ).first()

        discount = user_discount.value if user_discount else 0
        discount_price = round(product.price * (Decimal(1) - discount / Decimal(100)), 2)

        context["discount"] = discount
        context["discounted_price"] = discount_price

        return context

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Shoes
    success_url = reverse_lazy("products:list")
    permission_required = "products.delete_product"  # Определяем есть ли соответсвующие права на удаление продукта

