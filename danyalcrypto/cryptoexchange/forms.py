from django.forms import ModelForm
from .models import Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PurchaseForm(ModelForm):
    class Meta:
        model = Order
        fields = ['amount']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']