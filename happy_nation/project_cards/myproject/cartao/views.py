from django.shortcuts import render, redirect
from .forms import CartaoForm

def verificar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = CartaoForm()
    return render(request, 'cartao/verificar_cartao.html', {'form': form})

def sucesso(request):
    return render(request, 'cartao/sucesso.html')

def home(request):
    return render(request, 'cartao/home.html')