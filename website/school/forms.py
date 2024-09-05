from django import forms


from school.models.app_settings import AppSettingModel
from school.models.school import SchoolModel

class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolModel
        fields = ['name', 'url_logo','setting']  # Spécifie les champs à inclure dans le formulaire 

class AppSettingForm(forms.ModelForm):
    class Meta:
        model = AppSettingModel
        fields = ['smtp_server', 'smtp_port', 'smtp_username', 'smtp_password']                