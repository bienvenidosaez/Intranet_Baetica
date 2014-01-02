# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'proyectos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('f_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal(u'proyectos', ['Proyecto'])

        # Adding model 'Muro'
        db.create_table(u'proyectos_muro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Proyecto'])),
        ))
        db.send_create_signal(u'proyectos', ['Muro'])

        # Adding model 'Mensaje'
        db.create_table(u'proyectos_mensaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('muro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Muro'])),
            ('empleado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empleados.Empleado'])),
            ('texto', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('respuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Mensaje'], null=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['Mensaje'])

        # Adding model 'Tarea'
        db.create_table(u'proyectos_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('texto', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Proyecto'])),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Creador de la tarea', to=orm['empleados.Empleado'])),
            ('terminado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'proyectos', ['Tarea'])

        # Adding M2M table for field para on 'Tarea'
        m2m_table_name = db.shorten_name(u'proyectos_tarea_para')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tarea', models.ForeignKey(orm[u'proyectos.tarea'], null=False)),
            ('empleado', models.ForeignKey(orm[u'empleados.empleado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tarea_id', 'empleado_id'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'proyectos_proyecto')

        # Deleting model 'Muro'
        db.delete_table(u'proyectos_muro')

        # Deleting model 'Mensaje'
        db.delete_table(u'proyectos_mensaje')

        # Deleting model 'Tarea'
        db.delete_table(u'proyectos_tarea')

        # Removing M2M table for field para on 'Tarea'
        db.delete_table(db.shorten_name(u'proyectos_tarea_para'))


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
        u'empleados.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'proyectos.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empleados.Empleado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'muro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Muro']"}),
            'respuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Mensaje']", 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        u'proyectos.muro': {
            'Meta': {'object_name': 'Muro'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Proyecto']"})
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
        },
        u'proyectos.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Creador de la tarea'", 'to': u"orm['empleados.Empleado']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'para': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Destinatarios de la tarea'", 'symmetrical': 'False', 'to': u"orm['empleados.Empleado']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Proyecto']"}),
            'terminado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'texto': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['proyectos']