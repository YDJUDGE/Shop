from django.urls import path
from .views import show_profile_view, update_profile

urlpatterns = [
    path('user_profile/<int:pk>/', show_profile_view, name='show_profile'),
    path("update_profile/", update_profile, name="update_profile")
]

