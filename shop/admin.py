from asyncore import read
from django.contrib import admin

from shop.models import Worker, Shop, Visiting


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'worker', 'shop_name']
    search_fields = ['shop_name']

@admin.register(Visiting)
class VisitingAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'latitude', 'longitude']
    list_display_links = None
    search_fields = ['shop__worker__name', 'shop__shop_name']
    actions = None
    
    def has_add_permission(self, request, obj=None):
        return False