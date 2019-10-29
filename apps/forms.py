from django import forms
from .models import User, Group


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'group']


class GroupModelForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

