from django.urls import path

from .views import addutilisateur, modifierutilisateur, supprimerutilisateur, utilisateurlist


app_name = 'utilisateur'

urlpatterns=[
    path('', utilisateurlist, name='listutilisateur'),
    path('ajouterutilisateur/', addutilisateur, name='addutilisateur'),
    path('modifierutilisateur/<int:id>/', modifierutilisateur, name='modifierutilisateur'),
    path('supprimerutilisateur/<int:id>/', supprimerutilisateur, name='supprimerutilisateur')
]