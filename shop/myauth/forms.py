from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyCustomUser
from django import forms
from django.core.validators import MinLengthValidator

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Введите ваш email.")
    username = forms.CharField(min_length=4, max_length=60, help_text="Введите ваше имя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput, help_text="Пароль должен содержать не менее 8 символов")
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, help_text="Подтвердите пароль", validators=[MinLengthValidator(8)])

    class Meta:
        model = MyCustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
