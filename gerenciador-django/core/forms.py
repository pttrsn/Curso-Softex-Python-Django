from django import forms
from .models import Tarefa, Project

class TarefaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(TarefaForm, self).__init__(*args, **kwargs)
        if usuario:
            self.fields['projeto'].queryset = Project.objects.filter(usuario=usuario)
            
    class Meta:
        model = Tarefa
        fields = ['titulo', 'projeto', 'status']