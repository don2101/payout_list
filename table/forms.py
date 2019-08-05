from django import forms
from .models import Payout


class PayoutModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Payout
        fields = ['buyer', 'item', 'money']
