from django.urls import path

from school.views.school import addschool, checkschool, modifierschool, schoollist, supprimerschool
from school.views.app_setting import addsetting, check_settings, modifiersetting, settinglist, supprimersetting



app_name = 'school'

urlpatterns=[
    path('school/', schoollist, name='listschool'),
    path('checkschool/', checkschool, name='checkschool'),
    path('ajouterschool/', addschool, name='addschool'),
    path('modifierschool/<int:id>/', modifierschool, name='modifierschool'),
    path('supprimerschool/<int:id>/', supprimerschool, name='supprimerschool'),
    path('setting/', settinglist, name='settinglist'),
    path('', check_settings, name='checksetting'),
    path('modifiersetting/<int:id>/', modifiersetting, name='modifiersetting'),
    path('supprimersetting/<int:id>/', supprimersetting, name='supprimersetting'),
    path('parametre', addsetting, name='parametre'),
    ]