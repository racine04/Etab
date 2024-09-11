from django.urls import path

from .views import rapport,generate_pdf, generate_excel

app_name= 'rapport'

urlpatterns=[
    path('', rapport, name='rapport'),
    path('export/', generate_pdf, name='pdf'),
    path('excel/', generate_excel, name='excel'),
]