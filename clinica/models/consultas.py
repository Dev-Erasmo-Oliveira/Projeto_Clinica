from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from .paciente import Paciente
from .profissional import Profissional

class Consulta(models.Model):
    STATUS = (
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
        ('faltou', 'Faltou'),
    )
    @staticmethod
    def gerar_horarios():
        from datetime import time

        horarios = []
        hora = 8
        minuto = 0

        while hora < 17:
            horarios.append(
                (time(hora, minuto), f"{hora:02d}:{minuto:02d}")
            )

            minuto += 10
            if minuto == 60:
                minuto = 0
                hora += 1

        return horarios
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(
        Profissional,
        limit_choices_to={'tipo':'medico'},
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data = models.DateField()
    hora = models.TimeField(choices=gerar_horarios())
    status = models.CharField(max_length=20, choices=STATUS, default='agendada')
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data', 'hora']
        unique_together = ('medico', 'data', 'hora')
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora} - {self.medico}"

    # Função para nao permitir agendar nenhuma consulta no passado e nem com o mesmo medico em horários iguais


    def clean(self):
        if not self.data or not self.hora:
            return

        hoje = timezone.localdate()
        agora = timezone.localtime().time()

        # Não permitir consulta no passado
        if self.data < hoje:
            raise ValidationError("Não é possível agendar uma consulta no passado.")

        if self.data == hoje and self.hora <= agora:
            raise ValidationError("Não é possível agendar uma consulta em um horário já passado.")

        # Verificar conflito de horário (intervalo de 10 minutos)
        inicio_novo = datetime.combine(self.data, self.hora)
        fim_novo = inicio_novo + timedelta(minutes=10)

        consultas = Consulta.objects.filter(
            medico=self.medico,
            data=self.data
        )

        if self.pk:
            consultas = consultas.exclude(pk=self.pk)

        for consulta in consultas:
            inicio_existente = datetime.combine(consulta.data, consulta.hora)
            fim_existente = inicio_existente + timedelta(minutes=10)

            if inicio_novo < fim_existente and fim_novo > inicio_existente:
                raise ValidationError(
                    "Esse horário já está ocupado. O intervalo mínimo entre consultas é de 10 minutos."
                )