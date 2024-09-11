from django.urls import path
from professors.views.prof import addprof, modifierprof, proflist, supprimerprof


app_name= 'prof'

urlpatterns=[
    path('', proflist, name='proflist'),
    path('ajouterprofesseur/', addprof, name='addprof'),
    path('modifierprofesseur/<int:id>/', modifierprof, name='modifierprof'),
    path('supprimerprofesseur/<int:id>/', supprimerprof, name='supprimerprof'),
]