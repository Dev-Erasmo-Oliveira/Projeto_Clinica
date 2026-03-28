from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from clinica.models.consultas import Consulta
from clinica.models.paciente import Paciente
from clinica.forms import ConsultaForm, ConsultaStatusForm
from clinica.mixins import ApenasRecepcionistaMixin


class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'consultas/lista.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        return (
            Consulta.objects
            .select_related('paciente', 'medico')
            .order_by('-data', 'hora')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hoje = timezone.localdate()

        context['total_pacientes'] = Paciente.objects.count()
        context['consultas_hoje'] = Consulta.objects.filter(data=hoje).count()
        context['consultas_agendadas'] = Consulta.objects.filter(status='agendada').count()
        context['consultas_realizadas'] = Consulta.objects.filter(status='realizada').count()
        context['consultas_canceladas'] = Consulta.objects.filter(status='cancelada').count()
        context['consultas_faltou'] = Consulta.objects.filter(status = 'faltou').count()

        return context


class ConsultaCreateView(LoginRequiredMixin, ApenasRecepcionistaMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consultas/form.html'
    success_url = reverse_lazy('consultas-lista')
    
class ConsultaStatusUpdateView(LoginRequiredMixin, ApenasRecepcionistaMixin, UpdateView):
    model = Consulta
    form_class = ConsultaStatusForm
    template_name = 'consultas/status_form.html'
    success_url = reverse_lazy('consultas-lista')