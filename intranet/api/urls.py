from django.conf.urls import patterns, include, url
from api import empleado, cliente, proyecto

urlpatterns = patterns('',

    # Empleados
    url(r'^empleados/?$', empleado.empleado_api),
    url(r'^empleados/(?P<pk>[^/]+)/?$', empleado.empleado_api),

    # Clientes
    url(r'^clientes/?$', cliente.cliente_api),
    url(r'^clientes/(?P<pk>[^/]+)/?$', cliente.cliente_api),

    # Proyectos
    url(r'^proyectos/?$', proyecto.proyecto_api),
    url(r'^proyectos/(?P<pk>[^/]+)/?$', proyecto.proyecto_api),

)
