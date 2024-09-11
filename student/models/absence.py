from django.db import models

from base.models.helpers.datemodel import DateTimeModel
from student.models.student import StudentModel



class AbsenceModel(DateTimeModel):
 eleves = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='student_absence_id')
 absence_date= models.DateTimeField()
 absence_number = models.IntegerField()

 