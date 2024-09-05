from django.urls import path

from .views import signup, login_view

app_name= 'connexion'

urlpatterns=[
    path('', login_view, name='signin'),
    path('signup/', signup, name='signup')
]