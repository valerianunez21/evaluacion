from django import forms
from .models import Aprendiz
from .models import Materia

class AprendizForm(forms.ModelForm):
    class Meta: 
        model = Aprendiz
        fields = '__all__'

class MateriaForm(forms.ModelForm):
    class Meta: 
        model = Materia
        fields = '__all__'        