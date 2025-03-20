from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_cartao, name='verificar_cartao'),
    path('sucesso/', views.sucesso, name='sucesso'),
]