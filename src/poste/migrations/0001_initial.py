# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'poste_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('poste.fields.UUIDField')(max_length=64)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=4000, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('slug', self.gf('poste.fields.UUIDField')(db_index=False, max_length=250, blank=True)),
        ))
        db.send_create_signal(u'poste', ['Post'])

        # Adding model 'TextPost'
        db.create_table(u'poste_textpost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'poste', ['TextPost'])

        # Adding model 'ImagePost'
        db.create_table(u'poste_imagepost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'poste', ['ImagePost'])

        # Adding model 'Image'
        db.create_table(u'poste_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images_set', to=orm['poste.ImagePost'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=4000)),
        ))
        db.send_create_signal(u'poste', ['Image'])

        # Adding model 'CodePost'
        db.create_table(u'poste_codepost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('embed', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'poste', ['CodePost'])

        # Adding model 'QuotePost'
        db.create_table(u'poste_quotepost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'poste', ['QuotePost'])

        # Adding model 'LinkPost'
        db.create_table(u'poste_linkpost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'poste', ['LinkPost'])

        # Adding model 'ChatPost'
        db.create_table(u'poste_chatpost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('chat', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'poste', ['ChatPost'])

        # Adding model 'AudioPost'
        db.create_table(u'poste_audiopost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'poste', ['AudioPost'])

        # Adding model 'VideoPost'
        db.create_table(u'poste_videopost', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['poste.Post'], unique=True, primary_key=True)),
            ('embed', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'poste', ['VideoPost'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'poste_post')

        # Deleting model 'TextPost'
        db.delete_table(u'poste_textpost')

        # Deleting model 'ImagePost'
        db.delete_table(u'poste_imagepost')

        # Deleting model 'Image'
        db.delete_table(u'poste_image')

        # Deleting model 'CodePost'
        db.delete_table(u'poste_codepost')

        # Deleting model 'QuotePost'
        db.delete_table(u'poste_quotepost')

        # Deleting model 'LinkPost'
        db.delete_table(u'poste_linkpost')

        # Deleting model 'ChatPost'
        db.delete_table(u'poste_chatpost')

        # Deleting model 'AudioPost'
        db.delete_table(u'poste_audiopost')

        # Deleting model 'VideoPost'
        db.delete_table(u'poste_videopost')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'poste.audiopost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'AudioPost', '_ormbases': [u'poste.Post']},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'poste.chatpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'ChatPost', '_ormbases': [u'poste.Post']},
            'chat': ('django.db.models.fields.TextField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'poste.codepost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'CodePost', '_ormbases': [u'poste.Post']},
            'code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'embed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'poste.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images_set'", 'to': u"orm['poste.ImagePost']"})
        },
        u'poste.imagepost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'ImagePost', '_ormbases': [u'poste.Post']},
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'poste.linkpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'LinkPost', '_ormbases': [u'poste.Post']},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'poste.post': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('poste.fields.UUIDField', [], {'db_index': 'False', 'max_length': '250', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'blank': 'True'}),
            'uuid': ('poste.fields.UUIDField', [], {'max_length': '64'})
        },
        u'poste.quotepost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'QuotePost', '_ormbases': [u'poste.Post']},
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'source': ('django.db.models.fields.TextField', [], {})
        },
        u'poste.textpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'TextPost', '_ormbases': [u'poste.Post']},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'poste.videopost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'VideoPost', '_ormbases': [u'poste.Post']},
            'embed': ('django.db.models.fields.TextField', [], {}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['poste.Post']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['poste']