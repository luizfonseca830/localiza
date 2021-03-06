from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Locacao
from .forms import LocacaoForm


@login_required()
def locacoes_list(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacao.html', {'locacoes': locacoes})


@login_required()
def locacoes_new(request):
    form = LocacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        locacao = form.save()
        automovel = locacao.automovel
        automovel.alugado = True
        automovel.save()
        return redirect('locacoes_list')
    return render(request, 'locacao_form.html', {'form': form})


@login_required()
def locacoes_update(request, id):
    locacoes = get_object_or_404(Locacao, pk=id)
    form = LocacaoForm(request.POST or None, request.FILES or None, instance=locacoes)
    if form.is_valid():
        form.save()
        return redirect('locacoes_list')
    return render(request, 'locacao_form.html', {'form': form})


@login_required()
def locacoes_delete(request, id):
    locacao = get_object_or_404(Locacao, pk=id)

    if request.method == 'POST':
        locacao.delete()
        automovel = locacao.automovel
        automovel.alugado = False
        automovel.save()
        return redirect('locacoes_list')
    return render(request, 'locacao_delete_confirm.html', {'locacao': locacao})
