from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from professors.models.teacher import TeacherModel
from api.serializers.teacher_serializers import TeacherSerializer

@csrf_exempt

def teacher_list(request):

    if request.method == "GET":
        teacher = TeacherModel.objects.all()
        serializer= TeacherSerializer(teacher, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    
