# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FacebookLikebox.appId'
        db.add_column(u'cmsplugin_facebooklikebox', 'appId',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FacebookLikebox.appId'
        db.delete_column(u'cmsplugin_facebooklikebox', 'appId')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cms_social_facebook.facebookcomments': {
            'Meta': {'object_name': 'FacebookComments', 'db_table': "u'cmsplugin_facebookcomments'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'num_posts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'cms_social_facebook.facebookfacepile': {
            'Meta': {'object_name': 'FacebookFacepile', 'db_table': "u'cmsplugin_facebookfacepile'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'max_rows': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'cms_social_facebook.facebooklike': {
            'Meta': {'object_name': 'FacebookLike', 'db_table': "u'cmsplugin_facebooklike'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'border_color': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'arial'", 'max_length': '50'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'cms_social_facebook.facebooklikebox': {
            'Meta': {'object_name': 'FacebookLikebox', 'db_table': "u'cmsplugin_facebooklikebox'", '_ormbases': ['cms.CMSPlugin']},
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'border_color': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'cms_social_facebook.facebooklivestream': {
            'Meta': {'object_name': 'FacebookLivestream', 'db_table': "u'cmsplugin_facebooklivestream'", '_ormbases': ['cms.CMSPlugin']},
            'always_post_to_friends': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'event_app_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'via_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'xid': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'cms_social_facebook.facebookloginbutton': {
            'Meta': {'object_name': 'FacebookLoginButton', 'db_table': "u'cmsplugin_facebookloginbutton'", '_ormbases': ['cms.CMSPlugin']},
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'max_rows': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cms_social_facebook']