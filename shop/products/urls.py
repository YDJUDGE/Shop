from django.urls import path
from .views import ListProducts, ProductCreateView, ProductDeleteView, ProductDetailView

app_name = "products"

urlpatterns = [
    path("", ListProducts.as_view(template_name="products/shoe_list.html"), name="list"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("<int:pk>/confirm_delete/", ProductDeleteView.as_view(), name="delete_product"),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail_product")
]
