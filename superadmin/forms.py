from django import forms
from superadmin.models import Customers, Invoices

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        # fields = '__all__'
        fields = ['name','phone','email','address']

class InvoicesForm(forms.ModelForm):
    class Meta:
        model = Invoices
        # fields = '__all__'
        fields = ['customer','amount','date','status']