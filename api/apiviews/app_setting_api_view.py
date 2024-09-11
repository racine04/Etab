from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from user.models.user import UserModel
from api.serializers.user_serializers import UserSerializer


@csrf_exempt

def user_list(request):

    if request.method == "GET":
        teacher = UserModel.objects.all()
        serializer= UserSerializer(teacher, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    
