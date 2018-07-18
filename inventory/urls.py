from django.conf.urls import url
from .views import item, query_inventory, new_entry, new_item, new_withdrawal, \
                   entries, withdrawals


app_name = 'inventory'

urlpatterns = [
    url(r'^query_inventory/', query_inventory, name='query_inventory'),
    url(r'^item/(?P<piece_number>[\w\-]+)', item, name='item'),
    url(r'^new_item', new_item, name='new_item'),
    url(r'^new_entry/', new_entry, name='new_entry'),
    url(r'^new_withdrawal/', new_withdrawal, name='new_withdrawal'),
    url(r'^entries/', entries, name='entries'),
    url(r'^withdrawals/', withdrawals, name='withdrawals'),
]
