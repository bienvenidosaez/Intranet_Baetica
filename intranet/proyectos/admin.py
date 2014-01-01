from django.contrib import admin
from proyectos.models import Proyecto, Muro, Mensaje, Tarea


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'f_inicio', 'descripcion')

admin.site.register(Proyecto, ProyectoAdmin)


class MuroAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'proyecto')

admin.site.register(Muro, MuroAdmin)


class MensajeAdmin(admin.ModelAdmin):
    list_display = ('muro', 'empleado', 'texto', 'respuesta')

admin.site.register(Mensaje, MensajeAdmin)


class TareaAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'autor', 'terminado')

admin.site.register(Tarea, TareaAdmin)
