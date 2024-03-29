from django import forms
from .models import Fruit


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"

        widgets = {
            "fruit_name": forms.TextInput(attrs={"class":"form-control"}),
            "fruit_quan": forms.NumberInput(attrs={"class": "form-control"}),
            "delivery_address": forms.Textarea(attrs={"class": "form-control"}),
            "delivery_date": forms.DateInput(attrs={"class": "form-control"}),
            "payment_mode": forms.Select(attrs={"class": "form-control"}),
        }