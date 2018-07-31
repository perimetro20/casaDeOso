from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InventoryQueryForm, ItemForm, EntryForm, WithdrawalForm
from .models import Entry, Item, Withdrawal


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
            if form.cleaned_data['piece_number']:
                pn = form.cleaned_data['piece_number']
            elif form.cleaned_data['barcode_number']:
                barcode_number = form.cleaned_data['barcode_number']
                pn = get_object_or_404(Item, barcode_number=barcode_number).piece_number
            else:
                pn = 0
            return redirect('inventory:item',
                            piece_number=pn)
        else:
            return HttpResponseBadRequest


@login_required
def item(request, piece_number):
    item = get_object_or_404(Item,
                             piece_number=piece_number)
    context = {
        'item': item
    }
    return render(request, 'inventory/item.html', context)


@login_required
def edit_item(request, piece_number):
    item = get_object_or_404(Item,
                                 piece_number=piece_number)
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
            return redirect('inventory:item', piece_number=item.piece_number)
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
            'title': 'Dar Pieza de Alta',
            'action': 'Cargar Pieza',
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
                'title': 'Dar Pieza de Alta',
                'action': 'Cargar Pieza',
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


@login_required
def statistics(request):
    total = 0
    parts = Item.objects.all()
    for part in parts:
        total += part.cost * part.quantity
    context = {
        'total_cost': total
    }

    return render(request, 'inventory/statistics.html', context)
