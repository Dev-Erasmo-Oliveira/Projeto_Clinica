from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Validador simples para CPF (formato 000.000.000-00 ou apenas dígitos)
cpf_validator = RegexValidator(
    regex=r'^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$',
    message='CPF deve ter 11 dígitos (aceita com ou sem pontuação).'
)

class Paciente(models.Model):
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=14, unique=True, validators=[cpf_validator])
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome'] # coloquei isso para os pacientes virem organizados pelo nome sempre de A - Z
        verbose_name = 'Paciente'
        verbose_name_plural  = 'Pacientes'
    
    def __str__(self): # aqui estou definindo como o objeto será exibido como texto mais facil de entender, pra nao vir algo horrivel cheio de letra e número que é o padrão de vir
        return f'{self.nome} - {self.cpf}'
    
    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year

        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1

        return idade