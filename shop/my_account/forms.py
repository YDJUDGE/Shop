from django import forms
from .models import Profile

class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "vk", "twitter"]

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    vk = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    twitter = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'vk', 'twitter']

