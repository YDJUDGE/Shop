from django.shortcuts import render, redirect
from .models import Shoes
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import ProductCreateForm

class ListProducts(ListView):
    queryset = Shoes.objects.all()
    template_name = "products/shoe_list.html"
    context_object_name = "shoes"

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Shoes
    form_class = ProductCreateForm
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("products:list")

    def test_func(self):
        return self.request.user.is_staff

class ProductDetailView(DetailView):
    model = Shoes

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Shoes
    success_url = reverse_lazy("products:list")
    permission_required = "products.delete_product"  # Определяем есть ли соответсвующие права на удаление продукта

