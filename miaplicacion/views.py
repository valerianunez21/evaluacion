from django.shortcuts import render,redirect, get_object_or_404
from .forms import AprendizForm
from .models import Aprendiz

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def aprendices(request):
    lista = Aprendiz.objects.all()
    return render (request, 'aprendiz.html', {'lista': lista})

def eliminar(request,idaprendiz):
        dele= get_object_or_404(Aprendiz, idaprendiz = idaprendiz)
        dele.delete()
        return redirect(to='aprendices')

def formulario (request):
    data= {'form': AprendizForm()}
    if request.method == 'POST':
        formulario = AprendizForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('aprendices')
    return render(request, 'formulario.html', data)


def modificar(request, idaprendiz):
    apren = get_object_or_404(Aprendiz, idaprendiz=idaprendiz)
    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=apren)
        if form.is_valid():
            form.save()
            return redirect('aprendices')
    else:
        form = AprendizForm(instance=apren)
    
    return render(request, 'modificar.html', {'form': form, 'form_title': 'Modificar aprendiz'})