# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empleado'
        db.create_table(u'empleados_empleado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(max_length=10, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'empleados', ['Empleado'])


    def backwards(self, orm):
        # Deleting model 'Empleado'
        db.delete_table(u'empleados_empleado')


    models = {
        u'empleados.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['empleados']