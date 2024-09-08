from django.urls import path
from rest_framework import routers

from api.apiviews.student_api_view import student_list
from api.apiviews.teacher_api_view import teacher_list
from api.apiviews.user_api_view import user_list
from api.apiviews.index_api_view import index_api

router = routers.DefaultRouter()
#router.register(r'student', ca)

urlpatterns =[
    path('', index_api, name='index_api' ),
    path('student/', student_list, name='student' ),
    path('teacher/', teacher_list, name='teacher' ),
    path('user/', user_list, name='user' ),
]