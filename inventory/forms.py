from django import forms
from .models import Entry, Item, Withdrawal


class InventoryQueryForm(forms.Form):
    barcode_number = forms.CharField(label='Codigo de Barras',
                                     max_length=155,
                                     required=False)
    piece_number = forms.CharField(label='Número de Parte',
                                   max_length=155,
                                   required=False)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name',
                  'brand',
                  'piece_number',
                  'barcode_number',
                  'description',
                  'cost',
                  'quantity',
                  'unit']


class EntryForm(forms.Form):
    barcode_number = forms.CharField(label='Código de Barras',
                                     widget=forms.TextInput(attrs={'autofocus': 'autofocus'}),
                                     max_length=155,
                                     required=False)

    piece_number = forms.CharField(label='Número de Parte',
                                   max_length=155,
                                   required=False)

    quantity = forms.IntegerField(label='Número de piezas',
                                  required=True)

    bill_number = forms.CharField(label='Número de Factura',
                                  max_length=155,
                                  required=True)

    def clean(self):
        cleaned_data = super().clean()
        piece_number = cleaned_data.get('piece_number')
        barcode_number = cleaned_data.get('barcode_number')

        if not(piece_number or barcode_number):
            raise forms.ValidationError(
                    'Se tiene que rellenar el código de barras o el '
                    'número de pieza'
                )

        elif piece_number:
            if not Item.objects.filter(piece_number=piece_number).exists():
                raise forms.ValidationError(
                    'La pieza no existe, por favor dela de alta'
                )
        else:
            if not Item.objects.filter(barcode_number=barcode_number).exists():
                raise forms.ValidationError(
                    'La pieza no existe, por favor dela de alta'
                )

    def save(self):
        data = self.cleaned_data

        piece_number = data.get('piece_number')
        barcode_number = data.get('barcode_number')

        if piece_number:
            item = Item.objects.get(piece_number=piece_number)
        else:
            item = Item.objects.get(barcode_number=barcode_number)

        Entry.objects.create(item=item,
                             quantity=data.get('quantity'),
                             bill_number=data.get('bill_number'))


class WithdrawalForm(forms.Form):
    barcode_number = forms.CharField(label='Código de Barras',
                                     widget=forms.TextInput(attrs={'autofocus': 'autofocus'}),
                                     max_length=155,
                                     required=False)

    piece_number = forms.CharField(label='Número de Parte',
                                   max_length=155,
                                   required=False)

    quantity = forms.IntegerField(label='Número de Piezas',
                                  required=True)

    service_order = forms.CharField(label='Número de Orden de Servicio',
                                    max_length=155,
                                    required=True)

    employee = forms.CharField(label='Empleado:',
                               max_length=155)

    def clean(self):
        cleaned_data = super().clean()
        piece_number = cleaned_data.get('piece_number')
        barcode_number = cleaned_data.get('barcode_number')

        if not(piece_number or barcode_number):
            raise forms.ValidationError(
                    'Se tiene que rellenar el código de barras o el '
                    'número de parte'
                )
        elif piece_number:
            if not Item.objects.filter(piece_number=piece_number).exists():
                raise forms.ValidationError(
                    'La parte no existe, por favor dela de alta'
                )
            item = Item.objects.get(piece_number=piece_number)
        else:
            if not Item.objects.filter(barcode_number=barcode_number).exists():
                raise forms.ValidationError(
                    'La parte no existe, por favor dela de alta'
                )
            item = Item.objects.get(barcode_number=barcode_number)

        if cleaned_data.get('quantity') > item.quantity:
            raise forms.ValidationError(
                'No hay suficientes piezas en el inventario'
            )

    def save(self):
        data = self.cleaned_data

        piece_number = data.get('piece_number')
        barcode_number = data.get('barcode_number')

        if piece_number:
            item = Item.objects.get(piece_number=piece_number)
        else:
            item = Item.objects.get(barcode_number=barcode_number)

        Withdrawal.objects.create(item=item,
                                  quantity=data.get('quantity'),
                                  service_order=data.get('service_order'),
                                  employee=data.get('employee'))
