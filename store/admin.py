from django.contrib import admin

from store.models import Item, Tag, ItemTag


class TagInline(admin.TabularInline):
    model = Tag


class ItemTagInline(admin.TabularInline):
    model = ItemTag


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemTagInline]

    def tags(self):
        html = ""
        for obj in ItemTag.objects.filter(item__id=self.id):
            html += '<p><a href="%s">%s</a></p>' % (obj.tag.get_admin_url(), obj.tag)
        return html
    tags.allow_tags = True

    list_display = ('name', 'buy_dt', 'expires_dt', tags)

admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
