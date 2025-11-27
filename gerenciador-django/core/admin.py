from django.contrib import admin
from .models import Tarefa

# Register your models here.
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'usuario','status', 'data_criacao')
    list_filter = ('status', 'projeto', 'data_criacao')
    search_fields = ('titulo',)
    readonly_fields = ('data_criacao',)

    @admin.display(description='Email do Usuário') 
    def get_user_email(self, obj):
        return obj.user.email

admin.site.register(Tarefa, TarefaAdmin)