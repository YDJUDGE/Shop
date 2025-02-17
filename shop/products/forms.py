from django.forms import ModelForm, CharField
from .models import Shoes

class ProductCreateForm(ModelForm):
    class Meta:
        model = Shoes
        fields = ["name", "description", "brand", "price", "image"]
