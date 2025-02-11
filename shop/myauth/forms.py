from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyCustomUser
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Введите ваш email.")

    class Meta:
        model = MyCustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
