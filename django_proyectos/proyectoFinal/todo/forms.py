from dataclasses import fields
from django import forms
from .models import Tarea

#modelForm permite asociar el formulario al modelo, en este caso se asocia al modelo Tarea
class TareaForm(forms.ModelForm):
    
    #el valor tarea en la lista fields es para poder utilizar el campo de tarea del modelo Tarea, La clase meta le dice a la clase como comportarse
    class Meta:
        model = Tarea
        fields = ['tarea']