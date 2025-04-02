from django.shortcuts import render, redirect
from .forms import CartaoForm
from django.shortcuts import render, get_object_or_404


def verificar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            novo_cartao = form.save()
            return redirect('cartao:sucesso', cartao_id=novo_cartao.id)  # Note o namespace
    else:
        form = CartaoForm()
    return render(request, 'cartao/verificar_cartao.html', {'form': form})

def sucesso(request, cartao_id):
    cartao = get_object_or_404(cartao, id=cartao_id)
    return render(request, 'cartao/sucesso.html', {'cartao': cartao})
def home(request):
    return render(request, 'cartao/home.html')