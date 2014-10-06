from django import forms
from sistema.models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
