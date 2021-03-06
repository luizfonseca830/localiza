from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Automovel
from .forms import AutomovelForm


@login_required()
def automoveis_list(request):
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        automoveis =Automovel.objects.all()
        automoveis = Automovel.objects.filter(placa=termo_busca)
        automoveis = Automovel.objects.filter(modelo=termo_busca)
        automoveis = Automovel.objects.filter(marca=termo_busca)
    else:
        automoveis = Automovel.objects.all()
    return render(request, 'automovel.html', {'automoveis': automoveis})


@login_required()
def automoveis_locados(request):
    automoveislocados = Automovel.objects.filter(alugado=True)
    return render(request, 'automovel_locado.html', {'automoveislocados': automoveislocados})


@login_required()
def automoveis_new(request):
    form = AutomovelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('automovel_list')
    return render(request, 'automovel_form.html', {'form': form})


@login_required()
def automoveis_update(request, id):
    automovel = get_object_or_404(Automovel, pk=id)
    form = AutomovelForm(request.POST or None, request.FILES or None, instance=automovel)

    if form.is_valid():
        form.save()
        return redirect('automovel_list')
    return render(request, 'automovel_form.html', {'form': form})


@login_required()
def automoveis_delete(request, id):
    automovel = get_object_or_404(Automovel, pk=id)

    if request.method == 'POST':
        automovel.delete()
        return redirect('automovel_list')
    return render(request, 'automovel_delete_confirm.html', {'automovel': automovel})
