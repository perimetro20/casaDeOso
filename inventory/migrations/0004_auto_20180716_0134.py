# Generated by Django 2.0.4 on 2018-07-16 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_entries_withdrawals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='reference_number',
            new_name='piece_number',
        ),
    ]
