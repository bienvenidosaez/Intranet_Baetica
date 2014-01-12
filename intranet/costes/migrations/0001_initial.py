# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LineaCoste'
        db.create_table(u'costes_lineacoste', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('empleado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empleados.Empleado'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Proyecto'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('tiempo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'costes', ['LineaCoste'])


    def backwards(self, orm):
        # Deleting model 'LineaCoste'
        db.delete_table(u'costes_lineacoste')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '150'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'})
        },
        u'costes.lineacoste': {
            'Meta': {'ordering': "['proyecto', 'empleado']", 'object_name': 'LineaCoste'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empleados.Empleado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Proyecto']"}),
            'tiempo': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'})
        },
        u'empleados.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'p_hora': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '1'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'f_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['costes']