from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models.student import StudentModel
from professors.models.teacher import TeacherModel



# Create your views here.
@login_required(login_url='connexion:signup')
def rapport(request):
    return render(request, 'report/rapport.html')


