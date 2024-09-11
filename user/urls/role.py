from django.urls import path
from user.views.role import addrole, rolelist, supprimerrole


app_name = 'role'

urlpatterns=[
    path('role/', rolelist, name='listrole'),
    path('ajouterrole/', addrole, name='addrole'),
    path('supprimerrole/<int:id>/', supprimerrole, name='supprimerrole')
]