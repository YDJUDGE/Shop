from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm
from .models import MyCustomUser
from .utils import send_verification_email

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_verification_email(request, user)

            request.session['user_id'] = user.pk  # Запоминаем ID пользователя в сессии
            return redirect('verify_email')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def verify_email_view(request):
    user_id = request.session.get('user_id')
    verification_code = request.session.get("verification_code")
    if not user_id:
        return redirect('signup')

    user = MyCustomUser.objects.get(id=user_id)

    if request.method == "POST":
        entered_code = request.POST.get('code')

        if entered_code == user.verification_code:
            user.is_active = True
            user.verification_code = ""  # Очистка кода, чтобы он не хранился в БД
            user.save()

            del request.session["verification_code"]
            login(request, user)
            return redirect('products:list')
        else:
            return render(request, "registration/verify_email.html", {'error': 'Неверный код'})
    return render(request, "registration/verify_email.html")

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
