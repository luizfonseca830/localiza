from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm


@login_required()
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})


@login_required()
def clientes_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})


@login_required()
def clientes_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})


@login_required()
def clientes_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes _list')
    return render(request, 'cliente_delete_confirm.html', {'cliente': cliente})
