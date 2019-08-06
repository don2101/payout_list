from django import forms
from .models import Payout


class PayoutModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_field = ['buyer', 'item', 'money', 'buy_date']

        for field_name in update_field:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Payout
        fields = ['buyer', 'item', 'money', 'buy_date']
        