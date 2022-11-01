from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Tarefas
from .forms import AddTarefas, UserProfileForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import SetPasswordForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home_admin.html')

def jogos(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
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
            obj = form.save(commit=False)
            obj.usuario = request.user
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
            obj = form.save(commit=False)
            obj.usuario = request.user
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
            obj = form.save(commit=False)
            obj.usuario = request.user
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
            obj = form.save(commit=False)
            obj.usuario = request.user
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
            obj = form.save(commit=False)
            obj.usuario = request.user
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

def deletarTarefa(request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def publicar(request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.publicado = True 
    tarefas.save()   
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def usuarios(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']        
            group.user_set.add(user)
            
    else:
        form = UserProfileForm()       

    users = User.objects.all()
    context = {'users':users,'form':form}
    return render(request, 'usuarios.html', context)

def editUsuario(request, id):
    usuarios = User.objects.get(id = id)

    form = SetPasswordForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/usuarios/')

    users = User.objects.all()
    context = {'users':users,'form':form}
    return render(request, 'editUsers.html', context)


class deleteUser(DeleteView):
    model = User
    template_name='deleteEscolas.html'
    success_url = reverse_lazy('usuarios')