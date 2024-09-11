from django import forms

from base.models.adress import AddressModel


class AdressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = '__all__'  # Spécifie les champs à inclure dans le formulaire