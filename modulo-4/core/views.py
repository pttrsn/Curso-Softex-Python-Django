from django.shortcuts import render

def home(request):
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', context)

def login(request):
    return HttpResponse('<input>Login</input>')
