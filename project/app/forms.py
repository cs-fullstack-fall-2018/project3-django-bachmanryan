from django import forms
from .models import BankModel


class BankForm(forms.ModelForm):
    class Meta:
        model = BankModel
        fields = {'username'}
