from .models import OrderComment, Profile, Order
from django import forms
from django.contrib.auth.models import User

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

class MyDateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class UserOrderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'deadline']
        widgets = {"deadline": MyDateTimeInput}