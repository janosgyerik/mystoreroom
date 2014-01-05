from django.contrib import admin

from stock.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy_dt', 'expires_dt', )

admin.site.register(Item, ItemAdmin)
