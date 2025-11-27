from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]
    titulo = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    projeto = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    def __str__(self):
        return f"{self.titulo} ({self.status})"
