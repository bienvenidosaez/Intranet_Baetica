from django.contrib import admin
from empleados.models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'creado', 'modificado')

admin.site.register(Empleado, EmpleadoAdmin)
