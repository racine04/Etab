# eleve/urls.py
from django.urls import path
from .views import addeleve, elevelist, modifiereleve, supprimereleve

app_name = 'eleve'

urlpatterns = [
    path('', elevelist, name='elevelist'),
    path('ajoutereleve/', addeleve, name='addeleve'),
    path('modifiereleve/<int:id>/', modifiereleve, name='modifiereleve'),
    path('supprimereleve/<int:id>/', supprimereleve, name='supprimereleve'),
]
