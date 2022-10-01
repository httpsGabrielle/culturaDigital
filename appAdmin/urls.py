from appAdmin import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
]