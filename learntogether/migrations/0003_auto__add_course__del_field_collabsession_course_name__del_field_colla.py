# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'learntogether_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.TextField')()),
            ('course', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'learntogether', ['Course'])

        # Deleting field 'CollabSession.course_name'
        db.delete_column(u'learntogether_collabsession', 'course_name')

        # Deleting field 'CollabSession.course_url'
        db.delete_column(u'learntogether_collabsession', 'course_url')

        # Adding field 'CollabSession.course'
        db.add_column(u'learntogether_collabsession', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['learntogether.Course']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'learntogether_course')

        # Adding field 'CollabSession.course_name'
        db.add_column(u'learntogether_collabsession', 'course_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'CollabSession.course_url'
        db.add_column(u'learntogether_collabsession', 'course_url',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 5, 5, 0, 0), max_length=200),
                      keep_default=False)

        # Deleting field 'CollabSession.course'
        db.delete_column(u'learntogether_collabsession', 'course_id')


    models = {
        u'learntogether.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'badge_icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'learntogether.collabsession': {
            'Meta': {'object_name': 'CollabSession'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repeats_in_days': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'start_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'learntogether.collabsessionevent': {
            'Meta': {'object_name': 'CollabSessionEvent'},
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSession']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']", 'null': 'True', 'blank': 'True'}),
            'session_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'learntogether.collabsessioneventparticipant': {
            'Meta': {'object_name': 'CollabSessionEventParticipant'},
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSessionEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']"})
        },
        u'learntogether.course': {
            'Meta': {'object_name': 'Course'},
            'category': ('django.db.models.fields.TextField', [], {}),
            'course': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
        u'learntogether.groupmessage': {
            'Meta': {'object_name': 'GroupMessage'},
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSessionEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'learntogether.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_points': ('django.db.models.fields.IntegerField', [], {})
        },
        u'learntogether.userachievement': {
            'Meta': {'object_name': 'UserAchievement'},
            'achivement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.Achievement']"}),
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSession']", 'null': 'True', 'blank': 'True'}),
            'date_achieved': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']"})
        },
        u'learntogether.usergamepoint': {
            'Meta': {'object_name': 'UserGamePoint'},
            'collab_session_event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSessionEvent']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'default': "'Great Comment'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']"})
        }
    }

    complete_apps = ['learntogether']