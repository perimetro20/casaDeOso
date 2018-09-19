from django.urls import path
from django.conf.urls import url
from .views import item, query_inventory, new_entry, new_item, new_withdrawal, \
                   entries, sku, new_sku, edit_sku, withdrawals, edit_item, skus


app_name = 'inventory'

urlpatterns = [
    url(r'^query_inventory/', query_inventory, name='query_inventory'),
    path('skus/', skus, name='skus'),
    path('sku/<int:sku_id>/', sku, name='sku'),
    path('sku/new', new_sku, name='new_sku'),
    path('sku/<int:sku_id>/edit/', edit_sku, name='edit_sku'),
    url(r'^item/(?P<piece_number>[-\w /,]+)', item, name='item'),
    path('edit_item/<int:id>/)', edit_item, name='edit_item'),
    url(r'^new_item', new_item, name='new_item'),
    url(r'^new_entry/', new_entry, name='new_entry'),
    url(r'^new_withdrawal/', new_withdrawal, name='new_withdrawal'),
    url(r'^entries/', entries, name='entries'),
    url(r'^withdrawals/', withdrawals, name='withdrawals')
]
