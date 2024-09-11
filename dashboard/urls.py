from django.urls import path
from dashboard.views.dashboard import dashboard

app_name= 'dashboard'

urlpatterns=[
    path('', dashboard, name='dashboard'),
]