from django.urls import path
from .views import spin_wheel

urlpatterns = [
    path('wheel/', spin_wheel, name='wheel')
]
