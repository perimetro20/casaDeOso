from django.contrib import admin
from .models import Entry, Item, Withdrawal

admin.site.register(Item)
admin.site.register(Entry)
admin.site.register(Withdrawal)
