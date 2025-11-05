from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'nome_usuario': 'Petterson',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', context)

def login(request):
    return HttpResponse('<input>Login</input>')
