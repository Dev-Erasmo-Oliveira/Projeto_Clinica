from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from clinica.models import Paciente
from django.urls import reverse_lazy
from clinica.forms import PacienteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from clinica.mixins import ApenasRecepcionistaMixin


class PacienteCreateView(LoginRequiredMixin, ApenasRecepcionistaMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/form.html'
    success_url = reverse_lazy('pacientes-lista')
    
    
class PacienteUpdateView(LoginRequiredMixin, ApenasRecepcionistaMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/form.html'
    success_url = reverse_lazy('pacientes-lista')
    
class PacienteDeleteView(LoginRequiredMixin, ApenasRecepcionistaMixin, DeleteView):
    model = Paciente
    template_name = 'pacientes/delete.html'
    success_url = reverse_lazy('pacientes-lista')
     

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente    
    template_name = 'pacientes/lista.html'
    context_object_name = 'pacientes'