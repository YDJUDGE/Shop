from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})  # Перенаправление на страницу входа

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Проверка учётных данных
            if user is not None:
                login(request, user)
                return redirect('products:list')
    return render(request, 'registration/login.html', {'form': form})  # Перенаправление на страницу логина

def logout_view(request):
    logout(request)
    return redirect("login")
