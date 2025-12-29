from django.contrib import admin
from clinica.models import Paciente, Profissional, Consulta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'idade', 'telefone', 'email')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('data_nascimento',)


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'especialidade', 'criado_em')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'especialidade')
    list_filter = ('tipo',)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'paciente', 'medico', 'status')
    list_filter = ('data', 'status', 'medico')
    search_fields = ('paciente__nome', 'medico__user__username')
