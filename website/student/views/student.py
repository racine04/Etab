from django.shortcuts import get_object_or_404, redirect, render
from student.models.student import  StudentModel
from student.forms import MyFormStudent


def addeleve(request):
    if request.method == 'POST':
     form = MyFormStudent(request.POST)
     if form.is_valid():
        form.save()
        return redirect('eleve:elevelist')
    else:
       form = MyFormStudent()
    return render(request, 'eleves/ajoutereleve.html', {'form': form})


def elevelist(request):
    search_field= request.GET.get('search')
    if search_field :
        eleves = StudentModel.objects.filter(nom__icontains=search_field) | StudentModel.objects.filter(prenom__icontains=search_field)
        context = {
            'eleves': eleves,
            'search_field':search_field,
        }
    else:    
        eleves = StudentModel.objects.all()
        context = {
            'eleves': eleves,
        }
             
    return render(request, 'eleves/elevelist.html', context)

def modifiereleve(request, id):
    eleves = get_object_or_404(StudentModel, id=id)
    if request.method == 'POST':
        form = MyFormStudent(request.POST, instance=eleves)
        if form.is_valid():
            form.save()
            return redirect('eleve:elevelist')
    else:
        form = MyFormStudent(instance=eleves)
    return render(request, 'eleves/modifiereleve.html', {'form': form})

def supprimereleve(request, id):
    eleves = get_object_or_404(StudentModel, id=id)
    eleves.delete()
    return redirect('eleve:elevelist')