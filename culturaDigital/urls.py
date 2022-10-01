from django.contrib import admin
from django.urls import path, include
from appMain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('videos/', views.videos, name='videos'),
    path('games/', views.games, name='games'),
    path('atividades/', views.atividades, name='atividades'),
    
]