from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime, timedelta



class Profissional(models.Model):
    TIPOS = (
        ('medico', 'Médico'),
        ('recepcionista', 'Recepcionista'),
        ('admin', 'Administrador'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    especialidade = models.CharField(max_length=100, default='Clinico Geral', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        
    def __str__(self):
        return f"{self.user.username} ({self.tipo})"