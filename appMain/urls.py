from appMain import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('videos/', views.videos, name='videos'),
    path('games/', views.games, name='games'),
    path('atividades/', views.atividades, name='atividades'),
]