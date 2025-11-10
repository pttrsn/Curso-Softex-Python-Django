from django.shortcuts import render
from .models import Tarefa
from .models import Execucao

def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucao.objects.all()
    
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
        'execucao': todas_as_execucoes,
    }
    return render(request, 'home.html', context)