from django.contrib import admin

from store.models import Item, Tag, ItemTag


class TagInline(admin.TabularInline):
    model = Tag


class ItemTagInline(admin.TabularInline):
    model = ItemTag


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy_dt', 'expires_dt', )
    inlines = [ItemTagInline]

admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
