from django.shortcuts import render, get_object_or_404, redirect

from school.forms import SchoolForm
from school.models.school import SchoolModel


# Create your views here.

def addschool(request):
    if request.method == 'POST':
     form = SchoolForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('connexion:signin')
    else:
       form = SchoolForm()


    schools= SchoolModel.objects.all()
    if not schools :
        return render(request, 'school/ajouterschool.html', {'form':form})
    else :
        return redirect('connexion:signin') #connexion   

    

def schoollist(request):
    schools = SchoolModel.objects.all()
    return render(request, 'school/listschool.html', {'schools': schools})

def modifierschool(request, id):
    role = get_object_or_404(SchoolModel, id=id)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('school:listschool')
    else:
        form = SchoolForm(instance=role)
    return render(request, 'school/modifierschool.html', {'form': form})

def checkschool(request):
    schools= SchoolModel.objects.all()
    if not schools :
        return redirect('school:addschool')#ajouter ecole
    else :
        return redirect('connexion:signin')#connexion

def supprimerschool(request, id):
    role = get_object_or_404(SchoolModel, id=id)
    role.delete()
    return redirect('school:listschool')