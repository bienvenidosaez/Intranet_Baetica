from django.contrib import admin
from clientes.models import Cliente, Contacto


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'email', 'telefono')

admin.site.register(Cliente, ClienteAdmin)


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'empresa')

admin.site.register(Contacto, ContactoAdmin)
