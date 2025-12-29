from django.urls import path

from .views.login import LoginUsuarioView, LogoutUsuarioView

from .views.pacientes import (
    PacienteListView,
    PacienteCreateView,
    PacienteUpdateView,
    PacienteDeleteView,
)

from .views.consultas import (
    ConsultaListView,
    ConsultaCreateView,
)

from .views.medico_consultas_list import MedicoConsultasView


urlpatterns = [
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),

    path('pacientes/', PacienteListView.as_view(), name='pacientes-lista'),
    path('pacientes/novo/', PacienteCreateView.as_view(), name='pacientes-criar'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente-editar'),
    path('pacientes/<int:pk>/excluir/', PacienteDeleteView.as_view(), name='paciente-excluir'),

    path('consultas/', ConsultaListView.as_view(), name='consultas-lista'),
    path('consultas/nova/', ConsultaCreateView.as_view(), name='consultas-criar'),

    path('minhas-consultas/', MedicoConsultasView.as_view(), name='medico-consultas'),
]
