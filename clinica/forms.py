from django import forms
from django.utils import timezone

from .models.consultas import Consulta
from .models.profissional import Profissional
from .models.paciente import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data', 'hora', 'observacoes']

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'hora': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medico'].queryset = Profissional.objects.filter(tipo='medico')


class ConsultaStatusForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['status']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
        }