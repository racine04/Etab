from django.urls import path

from .views import modifierprof, proflist, addprof, supprimerprof

app_name= 'prof'

urlpatterns=[
    path('', proflist, name='proflist'),
    path('ajouterprofesseur/', addprof, name='addprof'),
    path('modifierprofesseur/<int:id>/', modifierprof, name='modifierprof'),
    path('supprimerprofesseur/<int:id>/', supprimerprof, name='supprimerprof')
]