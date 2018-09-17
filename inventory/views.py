from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InventoryQueryForm, SKUForm, ItemForm, EntryForm, WithdrawalForm
from .models import Entry, SKU, Item, Withdrawal


@login_required
def query_inventory(request):
    if request.method == "GET":
        form = InventoryQueryForm
        context = {
            'form': form
        }
        return render(request, 'inventory/query.html', context)
    elif request.method == "POST":
        form = InventoryQueryForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data['sku']
            id = get_object_or_404(SKU, sku=sku).id
            return redirect('inventory:sku',
                            sku_id=id)
        else:
            return HttpResponseBadRequest


@login_required
def sku(request, sku_id):
    sku = get_object_or_404(SKU, pk=sku_id)
    items = Item.objects.filter(sku=sku)
    context = {
        'sku': sku,
        'items': items
    }

    return render(request, 'inventory/sku.html', context)

@login_required
def new_sku(request):
    if request.method == 'GET':
        form = SKUForm
        context = {
            'title': 'Dar SKU de Alta',
            'action': 'Crear SKU',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = SKUForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:new_sku')
        else:
            context = {
                'title': 'Dar SKU de Alta',
                'action': 'Crear SKU',
                'form': form
            }

            return render(request, 'inventory/form.html', context)

@login_required
def edit_sku(request, sku_id):
    sku = get_object_or_404(SKU,
                            pk=sku_id)
    if request.method == 'GET':
        form = SKUForm(instance=sku)
        context = {
            'title': 'Editar SKU',
            'action': 'Editar SKU',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = SKUForm(request.POST, instance=sku)
        if form.is_valid():
            sku = form.save()
            return redirect('inventory:sku', sku_id=sku.id)
        else:
            context = {
                'title': 'Editar SKU',
                'action': 'Editar SKU',
                'form': form
            }
        return render(request, 'inventory/form.html', context)

@login_required
def item(request, piece_number):
    item = get_object_or_404(Item,
                             piece_number=piece_number)
    context = {
        'item': item
    }
    return render(request, 'inventory/item.html', context)


@login_required
def edit_item(request, id):
    item = get_object_or_404(Item,
                             id=id)
    if request.method == 'GET':
        form = ItemForm(instance=item)
        context = {
            'title': 'Editar Pieza',
            'action': 'Editar Pieza',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('inventory:item', id=item.id)
        else:
            context = {
                'title': 'Editar Pieza',
                'action': 'Editar Pieza',
                'form': form
            }
        return render(request, 'inventory/form.html', context)


@login_required
def new_item(request):
    if request.method == 'GET':
        form = ItemForm
        context = {
            'title': 'Cargar nuevo Item',
            'action': 'Cargar Item',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:new_item')
        else:
            context = {
                'title': 'Cargar Nuevo Item',
                'action': 'Cargar Item',
                'form': form
            }

            return render(request, 'inventory/form.html', context)


@login_required
def new_entry(request):
    if request.method == 'GET':
        form = EntryForm
        context = {
            'title': 'Introducir al Inventario',
            'action': 'Introducir al Inventario',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:new_entry')
        else:
            context = {
                'title': 'Introducir al Inventario',
                'action': 'Introducir al Inventario',
                'form': form
            }

            return render(request, 'inventory/form.html', context)


@login_required
def new_withdrawal(request):
    if request.method == 'GET':
        form = WithdrawalForm
        context = {
            'title': 'Retirar del Inventario',
            'action': 'Retirar del Inventario',
            'form': form
        }
        return render(request, 'inventory/form.html', context)
    elif request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:new_withdrawal')
        else:
            context = {
                'title': 'Retirar del Inventario',
                'action': 'Retirar del Inventario',
                'form': form
            }

            return render(request, 'inventory/form.html', context)


@login_required
def entries(request):
    all_entries = Entry.objects.all()
    context = {
        'word': 'Ingresos',
        'items': all_entries
    }
    return render(request, 'inventory/history.html', context)


@login_required
def withdrawals(request):
    all_withdrawals = Withdrawal.objects.all()
    context = {
        'word': 'Egresos',
        'items': all_withdrawals
    }
    return render(request, 'inventory/history.html', context)
