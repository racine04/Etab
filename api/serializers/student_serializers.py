from rest_framework import serializers
from student.models.student import StudentModel


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = "__all__"