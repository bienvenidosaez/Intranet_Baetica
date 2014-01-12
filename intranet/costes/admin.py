from django.contrib import admin
from .models import LineaCoste


class LineaCosteAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'proyecto', 'descripcion', 'tiempo', 'creado', 'modificado')

admin.site.register(LineaCoste, LineaCosteAdmin)
