from django.views.generic import ListView, CreateView
from clinica.models import Consulta
from django.urls import reverse_lazy
from clinica.forms import ConsultaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from clinica.mixins import ApenasRecepcionistaMixin

class ConsultaListView(LoginRequiredMixin,ListView):
    model = Consulta
    template_name = 'consultas/lista.html'
    context_object_name = 'consultas'
    

class ConsultaCreateView(LoginRequiredMixin, ApenasRecepcionistaMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/form.html'
    success_url = reverse_lazy('consultas-lista')