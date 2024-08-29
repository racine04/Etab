from django.shortcuts import render

# Create your views here.
def rapport(request):
    return render(request, 'rapport.html')
