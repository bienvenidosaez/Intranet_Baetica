from django.contrib import admin
from empleados.models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'p_hora')

admin.site.register(Empleado, EmpleadoAdmin)
