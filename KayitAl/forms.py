from django import forms

from .models import KayitModels

class KayitForm(forms.ModelForm):

    class Meta:
        model = KayitModels
        fields = ('adi', 'soyadi','cinsiyet','tcKimlikNo')

