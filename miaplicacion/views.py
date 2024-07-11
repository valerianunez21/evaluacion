from django.shortcuts import render,redirect, get_object_or_404
from .forms import AprendizForm
from .forms import MateriaForm
from .models import Aprendiz,Materia

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def aprendices(request):
    lista = Aprendiz.objects.all()
    return render (request, 'aprendiz.html', {'lista': lista})

def eliminar(request,idaprendiz):
        dele= get_object_or_404(Aprendiz, idaprendiz = idaprendiz)
        dele.delete()
        return redirect(to='aprendiz')

def formulario (request):
    data= {'form': AprendizForm()}
    if request.method == 'POST':
        formulario = AprendizForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('aprendiz')
    return render(request, 'formulario.html', data)


def modificar(request, idaprendiz):
    apren = get_object_or_404(Aprendiz, idaprendiz=idaprendiz)
    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=apren)
        if form.is_valid():
            form.save()
            return redirect('aprendiz')
    else:
        form = AprendizForm(instance=apren)
    
    return render(request, 'modificar.html', {'form': form, 'form_title': 'Modificar aprendiz'})




def materias(request):
    list = Materia.objects.all()
    return render (request, 'materia.html', {'list': list})

def eliminarmat(request,idmateria):
        delet= get_object_or_404(Materia, idmateria = idmateria)
        delet.delete()
        return redirect(to='materia')

def formulariodos (request):
    datab= {'form': MateriaForm()}
    if request.method == 'POST':
        formulario2 = MateriaForm(datab=request.POST)
        if formulario2.is_valid():
            formulario2.save()
            return redirect('materia')
    return render(request, 'formulario2.html', datab)


def modificarmat(request, idamateria):
    mate = get_object_or_404(Materia, idmateria=idamateria)
    if request.method == 'POST':
        formu = MateriaForm(request.POST, instance=mate)
        if formu.is_valid():
            formu.save()
            return redirect('materia')
    else:
        formu = MateriaForm(instance=mate)
    
    return render(request, 'modificar2.html', {'form': formu, 'form_title': 'Modificar materia'})