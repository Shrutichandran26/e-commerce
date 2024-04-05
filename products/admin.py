from django.contrib import admin
from.models import Item
class ItemsAdmin(admin.ModelAdmin):
    list_display=('name','price','image')
admin.site.register(Item,ItemsAdmin)
