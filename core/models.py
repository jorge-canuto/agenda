from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #black: o campo pode estar em branco. null: o campo pode ser nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #verbose_name: nome mostrado na listagem de eventos do django admin
    data_criacao = models.DateTimeField(auto_now=True) #auto_now: insere automaticamente a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo