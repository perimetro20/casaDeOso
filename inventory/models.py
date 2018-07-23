from django.db import models


class Item(models.Model):
    GASOLINA = 'gasolina'
    PRODUCTO_TERMINADO = 'producto_terminado'
    ACCESORIOS = 'accesorios'
    REFACCIONES = 'refacciones'
    AREA_OPTIONS = ((GASOLINA, 'Gasolina'),
                       (PRODUCTO_TERMINADO, 'Producto Terminado'),
                       (ACCESORIOS, 'Accesorios'),
                       (REFACCIONES, 'Refacciones'))

    name = models.CharField(max_length=155,
                            verbose_name='Nombre')
    brand = models.CharField(max_length=155,
                             verbose_name='Marca',
                             blank=True)
    area = models.TextField(choices=AREA_OPTIONS, verbose_name='Área')
    piece_number = models.CharField(max_length=155,
                                    unique=True,
                                    verbose_name='Número de Parte')
    barcode_number = models.CharField(max_length=155,
                                      default='',
                                      blank=True,
                                      verbose_name='Código de barras')
    description = models.TextField(verbose_name='Descripción')
    cost = models.DecimalField(max_digits=12,
                               decimal_places=2,
                               verbose_name='Costo')
    quantity = models.IntegerField(default=0,
                                   verbose_name='Cantidad')
    unit = models.CharField(max_length=155,
                            verbose_name='Unidad')

    def __str__(self):
        return self.piece_number

    def verbose_area_name(self):
        if self.area == self.GASOLINA:
            return 'Gasolina'
        elif self.area == self.PRODUCTO_TERMINADO:
            return 'Producto Terminado'
        elif self.area == self.ACCESORIOS:
            return 'Accesorios'
        elif self.area == self.REFACCIONES:
            return 'Refacciones'

class Entry(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    bill_number = models.CharField(max_length=155,
                                   verbose_name='Número de Factura')

    def save(self, *args, **kwargs):
        """ Override the save method to add the capturista group.
        """
        if self.pk is None:
            item = self.item
            item.quantity += self.quantity
            item.save()
        return super(Entry, self).save(*args, **kwargs)


class Withdrawal(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    service_order = models.CharField(max_length=155)
    employee = models.CharField(max_length=155,
                                blank=True)

    def save(self, *args, **kwargs):
        """ Override the save method to add the capturista group.
        """
        if self.pk is None:
            item = self.item
            item.quantity -= self.quantity
            item.save()
        return super(Withdrawal, self).save(*args, **kwargs)
