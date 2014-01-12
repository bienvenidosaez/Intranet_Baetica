# Gestor de proyectos en Django y Backbone

## Instalación de archivos estáticos
- bower install
- npm install
- ./manage.py collectstatic --settings=intranet.settings.local

###Django
- ./manage.py runserver --settings=intranet.settings.local
- ./manage.py validate --settings=intranet.settings.local

####Shell
- ./manage.py shell --settings=intranet.settings.local
- ./manage.py createsuperuser --setting=intranet.settings.local


####Mockups
Creación de modelos
- ./manage.py mockups app.Model:n --setting=intranet.settings.local

####South
Creación de migraciones
- ./manage.py schemamigration empleados --auto --settings=intranet.settings.local
- ./manage.py schemamigration costes --initial --settings=intranet.settings.local
Migrar
- ./manage.py migrate costes --setting=intranet.settings.local

###Alias
- alias a_local='./manage.py runserver --settings=intranet.settings.local'
- alias v_local='./manage.py validate --settings=intranet.settings.local'
- alias s_local='./manage.py shell --settings=intranet.settings.local'
- source .bash_profile


## License

Everything in this repo is MIT License unless otherwise specified.

MIT © Bienvenido Sáez Muelas
