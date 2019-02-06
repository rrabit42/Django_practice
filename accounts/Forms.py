from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    class Meta(UserCreationForm.Meta):
        fields= UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        profile = Profile.objects.creat(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'],
        )
        return user

