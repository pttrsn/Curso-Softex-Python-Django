from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'concluida', 'data_criacao')
    list_filter = ('concluida', 'user', 'data_criacao')
    search_fields = ('titulo', 'user__username')
    fieldsets = (
('Informações Principais', {
'fields': ('user', 'titulo')
}),
('Status da Tarefa', {
'fields': ('concluida', 'data_criacao')
}),
)

readonly_fields = ('data_criacao')
admin.site.register(Tarefa,TarefaAdmin)
