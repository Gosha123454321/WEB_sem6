from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Book


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=255)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publication_year']