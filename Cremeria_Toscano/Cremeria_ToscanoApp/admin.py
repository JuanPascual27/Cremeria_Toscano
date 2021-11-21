from django.contrib import admin

# Register your models here.

admin.site.site_header="DB Cremeria_Toscano"
admin.site.site_title="DB Cremeria_Toscano"
admin.site.index_title="Cremeria_Toscano"

from .models import *
admin.site.register(Clientes)
admin.site.register(Compras)
admin.site.register(Detallescompras)
admin.site.register(Detallesventas)
admin.site.register(Proveedores)
admin.site.register(Rutas)
admin.site.register(Vendedores)
admin.site.register(Ventas)

class ProductosCT(admin.ModelAdmin):
	list_display=["idproducto","nombreproducto","detalles"]
	search_fields=["idproducto","nombreproducto","detalles"]

admin.site.register(Productos, ProductosCT)