from django import forms
from superadmin.models import Customers, Invoices

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

class InvoicesForm(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = '__all__'