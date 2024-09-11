from django.urls import path

from .views import checklogin, signup, login_view,logout_view

app_name= 'connexion'

urlpatterns=[
    path('', login_view, name='signin'),
    path('signup/', signup, name='signup'),
    path('checklogin/', checklogin, name='checklogin'),
    path('logout/', logout_view, name='logout'),
]