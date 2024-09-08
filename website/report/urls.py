from django.urls import path

from .views import rapport

app_name= 'rapport'

urlpatterns=[
    path('', rapport, name='rapport'),
]