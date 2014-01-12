from django.conf.urls import *

#Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^$', prueba),
    url(r'^api/', include('api.urls')),

    #Urls para el admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
)
