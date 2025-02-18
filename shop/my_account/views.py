from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from myauth.models import MyCustomUser
from django.contrib.auth.decorators import login_required
from .forms import CreateProfile, UpdateProfileForm
from django.db.models.signals import post_save  # сигнал, который срабатывает, после сохранения объекта
from django.dispatch import receiver  # привязывает функцию к определённому сигналу

@login_required
def show_profile_view(request, pk):
    user_account = get_object_or_404(Profile, user_id=pk)
    return render(request, template_name="m_account/user_profile.html", context={"user_account": user_account})


@receiver(post_save, sender=MyCustomUser)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

@login_required
def update_profile(request):
    profile = request.user.profile  # получение профиля юзера
    form = CreateProfile(request.POST or None, request.FILES or None, instance=profile)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('show_profile', pk=request.user.pk)

    return render(request, 'm_account/update_profile.html', {'form': form})
