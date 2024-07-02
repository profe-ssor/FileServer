from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email',  'password1', 'password2']

class WeddingForm(forms.ModelForm):
    class Meta:
        model = WeddingCards
        fields = ['title', 'description', 'uploaded_date', 'email', 'upload_card']

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionForms
        fields = ['title', 'description', 'uploaded_date', 'email', 'upload_card']

class EngagementForm(forms.ModelForm):
    class Meta:
        model = EngagementCards
        fields = ['title', 'description', 'uploaded_date', 'email', 'upload_card']

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = BirthdayCards
        fields = ['title', 'description', 'uploaded_date', 'email', 'upload_card']

