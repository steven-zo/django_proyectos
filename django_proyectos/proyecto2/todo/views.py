from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import AgregarTarea

# Create your views here.

tareas = []

def home(request):
    context = {'tareas':tareas}
    return render(request, 'todo/home.html', context)

def add(request):
    #Se valida si la peticion es POST y se recibe la info del formulario
    if request.method == 'POST':
        form = AgregarTarea(request.POST) #campo del formulario y se pone el request.post para leer el contenido de ese campo
        if form.is_valid(): #se valida el contenido del campo
            tarea = form.cleaned_data["tarea"] #se guarda el texto en una variable, adentro de las llaves va el nombre del campo definido en el archivo de forms
            tareas.append(tarea) #se agrega esa tarea a la lista tareas
            return redirect('home')
    #Si es GET entonces se devuelve el form vacio
    else:
        form = AgregarTarea()
    context = {'form':form}
    return render(request, 'todo/add.html', context)
