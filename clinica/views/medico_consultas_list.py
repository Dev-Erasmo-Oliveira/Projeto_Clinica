from django.views.generic import ListView
from clinica.models import Consulta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class MedicoConsultasView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'consultas/medico_lista.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        profissional = self.request.user.profissional
        if profissional.tipo != 'medico':
            raise PermissionDenied

        return (
            Consulta.objects
            .filter(medico=profissional)
            .order_by('data', 'hora')
        )