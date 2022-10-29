from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import Recipe, Review


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class MyForm(forms.ModelForm):
    class Meta:
        model = Recipe

        fields = ["fullname", "Time", "Difficulty","categoriesss", "ResText", "Ingredients","upload","author"]
        labels = {'fullname': "Name", "Time": "Time to Cook", "Difficulty": "Difficulty", "ResText": "Instructions"
            , "Ingredients": "Ingredients","categoriesss":"Categories","upload":"upload","author":"author"}


class MyForm2(forms.ModelForm):
    class Meta:
        model = Review

        fields = ["name", "date", "Text"]
        labels = {'name': "name", "date": "date", "Text": "Text"}
