from django.db import models

from base.models.helpers.datemodel import DateTimeModel

from .student import  StudentModel

class StudentCardModel(DateTimeModel):
    reference = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference