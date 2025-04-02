from django.urls import path
from . import views

app_name = 'cartao'  # Namespace importante!

urlpatterns = [
    path('verificar/', views.verificar_cartao, name='verificar_cartao'),
    path('sucesso/<int:cartao_id>/', views.sucesso, name='sucesso'),  # Note o parâmetro cartao_id
]