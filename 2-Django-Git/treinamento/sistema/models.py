from django.db import models

# Create your models here.


class Todo(models.Model):
    """docstring to Todo"""
    tarefa = models.CharField(max_length=128)
    completa = models.BooleanField(default=False)
