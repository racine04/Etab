from django.shortcuts import render

def index_api(request):
    return render(request, 'api/api_list.html')