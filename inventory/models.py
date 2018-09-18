from django.db import models


class SKU(models.Model):
    sku = models.CharField(max_length=155,
                           verbose_name='SKU')
    name = models.CharField(max_length=155,
                            verbose_name='Nombre')
    brand = models.CharField(max_length=155,
                             verbose_name='Marca',
                             blank=True)
    modelo = models.CharField(max_length=155,
                              verbose_name='Modelo',
                              blank=True)
    description = models.TextField(verbose_name='Descripción')
    part_number = models.CharField(max_length=155,
                                   verbose_name='Número de Parte',
                                   blank=True)
    height = models.IntegerField(verbose_name='Alto')
    width = models.IntegerField(verbose_name='Ancho')
    length = models.IntegerField(verbose_name='Largo')
    measuring_unit = models.CharField(max_length=155,
                                      verbose_name='Unidad de Medida')

    def __str__(self):
        return self.sku

class Item(models.Model):
    sku = models.ForeignKey('SKU', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Número')
    location = models.CharField(max_length = 255,
                                verbose_name = 'Ubicación')
    serial_number = models.CharField(max_length=255,
                                     verbose_name='Número de Serie',
                                     blank=True)
    individual_details = models.TextField(verbose_name='Detalles Individuales',
                                          blank=True)
    appraisal = models.DecimalField(max_digits=12,
                                    decimal_places=2,
                                    verbose_name='Costo Estimado',
                                    null=True)

    def __str__(self):
        return self.piece_number


class Picture(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)


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
