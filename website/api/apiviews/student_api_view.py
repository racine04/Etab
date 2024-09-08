from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from api.serializers.student_serializers import StudentSerializer
from student.models.student import StudentModel

@csrf_exempt

def student_list(request):

    if request.method == "GET":
        student = StudentModel.objects.all()
        serializer= StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    
