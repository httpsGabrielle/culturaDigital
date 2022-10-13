from django.utils.translation import gettext_lazy as _
from django import forms
from django.db.models import fields
from appMain.models import Tarefas
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class AddTarefas(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = '__all__'
