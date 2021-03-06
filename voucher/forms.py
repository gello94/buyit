from django import forms
from .models import Voucher


class VoucherForm(forms.Form):
    code = forms.CharField()


class AddNewVoucher(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ('code', 'amount', 'active')