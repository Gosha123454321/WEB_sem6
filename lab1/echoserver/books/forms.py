from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Book

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'name', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publication_year']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'name']