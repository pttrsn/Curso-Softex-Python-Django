from django import forms
from .models import Tarefa
from projects.models import Project

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo',]