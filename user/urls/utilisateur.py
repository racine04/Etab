from django.urls import path
from user.views.utilisateur import addutilisateur, modifierutilisateur, supprimerutilisateur, utilisateurlist
from user.views.role import addrole, modifierrole, rolelist, supprimerrole


app_name = 'utilisateur'

urlpatterns=[
    path('', utilisateurlist, name='listutilisateur'),
    path('ajouterutilisateur/', addutilisateur, name='addutilisateur'),
    path('modifierutilisateur/<int:id>/', modifierutilisateur, name='modifierutilisateur'),
    path('supprimerutilisateur/<int:id>/', supprimerutilisateur, name='supprimerutilisateur'),
    path('role/', rolelist, name='listrole'),
    path('ajouterrole/', addrole, name='addrole'),
    path('modifierrole/<int:id>/', modifierrole, name='modifierrole'),
    path('supprimerrole/<int:id>/', supprimerrole, name='supprimerrole'),
    
]