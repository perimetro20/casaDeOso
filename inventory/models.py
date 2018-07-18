from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=155,
                            verbose_name='Nombre')
    brand = models.CharField(max_length=155,
                             verbose_name='Marca',
                             blank=True)
    piece_number = models.CharField(max_length=155,
                                    unique=True,
                                    verbose_name='Número de Parte')
    barcode_number = models.CharField(max_length=155,
                                      default='',
                                      unique=True,
                                      blank=True,
                                      verbose_name='Código de barras')
    description = models.TextField(verbose_name='Descripción')
    cost = models.DecimalField(max_digits=12,
                               decimal_places=2,
                               verbose_name='Costo')
    quantity = models.IntegerField(default=0,
                                   verbose_name='Cantidad')

    def __str__(self):
        return self.piece_number


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
