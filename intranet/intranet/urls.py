from django.conf.urls import *

#Admin
from django.contrib import admin
admin.autodiscover()

#rest framework
from rest_framework import routers
from clientes.views import ClienteViewSet
from empleados.views import EmpleadoViewSet
from proyectos.views import ProyectoViewSet

from empleados.views import prueba

router = routers.DefaultRouter()
router.register(r'empleados',  EmpleadoViewSet)
router.register(r'proyectos',  ProyectoViewSet)
router.register(r'clientes',   ClienteViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', prueba),
    # url(r'^blog/', include('blog.urls')),

    #rest framework
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Urls para el admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
)
