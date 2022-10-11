from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Tarefas
from appMain.views import tarefas
from .forms import AddTarefas
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

def jogos(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/jogos/')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repojogos.html', context)

def jogospendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/jogos/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'jogos_pendentes.html', context)

def videos(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/videos/')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repovideos.html', context)

def videospendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/videos/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'videos_pendentes.html', context)

def atividades(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/atividades')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repoativ.html', context)

def atividadespendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/atividades/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'atividades_pendentes.html', context)

def edit(request, id):
    tarefas = Tarefas.objects.get(id = id)

    form = AddTarefas(request.POST or None, instance=tarefas)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/jogos/')
    
    context = {'tarefas':tarefas, 'form':form}
    return render(request, 'edit.html', context)

def escolas(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'escolas.html', context)