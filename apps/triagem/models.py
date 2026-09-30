from django.db import models

# Create your models here.
class Paciente(models.Model):
    codigo_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sintomas = models.TextField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.nome