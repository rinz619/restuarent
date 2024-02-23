from django import forms
from superadmin.models import Customers, Invoices

class customerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

class invoiceForm(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = '__all__'