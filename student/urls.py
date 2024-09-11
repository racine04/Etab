# eleve/urls.py
from django.urls import path

from student.views.absence import absencelist, addabsence, modifierabsence, supprimerabsence
from student.views.card import addcard, cardlist, modifiercard, supprimercard
from student.views.student import addeleve, elevelist, modifiereleve, supprimereleve


app_name = 'eleve'

urlpatterns = [
    path('', elevelist, name='elevelist'),
    path('card/', cardlist, name='cardlist'),
    path('absence/', absencelist, name='absencelist'),
    path('ajoutereleve/', addeleve, name='addeleve'),
    path('ajouterabsence/', addabsence, name='addabsence'),
    path('creercarte/', addcard, name='addcard'),
    path('modifiereleve/<int:id>/', modifiereleve, name='modifiereleve'),
    path('modifierabsence/<int:id>/', modifierabsence, name='modifierabsence'),
    path('modifiercard/<int:id>/', modifiercard, name='modifiercard'),
    path('supprimereleve/<int:id>/', supprimereleve, name='supprimereleve'),
    path('supprimercard/<int:id>/', supprimercard, name='supprimercard'),
    path('supprimerabsence/<int:id>/', supprimerabsence, name='supprimerabsence'),
]
