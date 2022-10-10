from django.utils.translation import gettext_lazy as _
from django import forms
from django.db.models import fields
from appMain.models import Tarefas

class AddTarefas(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = '__all__'
        