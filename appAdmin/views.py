from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Materia, Categoria, Tarefas

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

