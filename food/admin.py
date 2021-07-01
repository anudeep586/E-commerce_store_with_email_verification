from django.contrib import admin
from .models import Pizza,Salads,Noodles,Order


admin.site.site_header="Peace Tech House"
admin.site.site_title="Peace Tech"
admin.site.index_title="Manage customer Shopping"

class OrdersAdmin(admin.ModelAdmin):
    list_display=('name','price','id')
    search_fields=('name',)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','state','total')
    search_fields=('name',)

admin.site.register(Pizza,OrdersAdmin)
admin.site.register(Salads)
admin.site.register(Noodles)
admin.site.register(Order,CustomerAdmin)