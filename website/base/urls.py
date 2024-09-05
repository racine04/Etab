from django.urls import path

from base.view import addadress, adresslist, modifieradress, supprimeradress

app_name= 'adress'

urlpatterns =[
    path('adress/', adresslist, name='adresslist'),
    path('ajouteradress/', addadress, name='addadress'),
    path('modifieradress/<int:id>/', modifieradress, name='modifieradress'),
    path('supprimeradress/<int:id>/', supprimeradress, name='supprimeradress')
]