# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserGamePoint.collab_session'
        db.delete_column(u'learntogether_usergamepoint', 'collab_session_id')

        # Adding field 'UserGamePoint.collab_session_event'
        db.add_column(u'learntogether_usergamepoint', 'collab_session_event',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSessionEvent'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'CollabSessionEvent.start_time'
        db.alter_column(u'learntogether_collabsessionevent', 'start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'CollabSessionEvent.end_time'
        db.alter_column(u'learntogether_collabsessionevent', 'end_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'CollabSessionEvent.session_date'
        db.alter_column(u'learntogether_collabsessionevent', 'session_date', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'CollabSessionEvent.leader'
        db.alter_column(u'learntogether_collabsessionevent', 'leader_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.User'], null=True))

        # Changing field 'CollabSessionEventParticipant.collab_session'
        db.alter_column(u'learntogether_collabsessioneventparticipant', 'collab_session_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSessionEvent']))
        # Deleting field 'CollabSession.course_soure'
        db.delete_column(u'learntogether_collabsession', 'course_soure')

        # Adding field 'CollabSession.course_url'
        db.add_column(u'learntogether_collabsession', 'course_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


        # Changing field 'CollabSession.start_time'
        db.alter_column(u'learntogether_collabsession', 'start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'CollabSession.start_date'
        db.alter_column(u'learntogether_collabsession', 'start_date', self.gf('django.db.models.fields.DateField')(auto_now=True))

    def backwards(self, orm):
        # Adding field 'UserGamePoint.collab_session'
        db.add_column(u'learntogether_usergamepoint', 'collab_session',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'UserGamePoint.collab_session_event'
        db.delete_column(u'learntogether_usergamepoint', 'collab_session_event_id')


        # Changing field 'CollabSessionEvent.start_time'
        db.alter_column(u'learntogether_collabsessionevent', 'start_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'CollabSessionEvent.end_time'
        db.alter_column(u'learntogether_collabsessionevent', 'end_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 5, 0, 0)))

        # Changing field 'CollabSessionEvent.session_date'
        db.alter_column(u'learntogether_collabsessionevent', 'session_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'CollabSessionEvent.leader'
        db.alter_column(u'learntogether_collabsessionevent', 'leader_id', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2013, 5, 5, 0, 0), to=orm['learntogether.User']))

        # Changing field 'CollabSessionEventParticipant.collab_session'
        db.alter_column(u'learntogether_collabsessioneventparticipant', 'collab_session_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession']))
        # Adding field 'CollabSession.course_soure'
        db.add_column(u'learntogether_collabsession', 'course_soure',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)

        # Deleting field 'CollabSession.course_url'
        db.delete_column(u'learntogether_collabsession', 'course_url')


        # Changing field 'CollabSession.start_time'
        db.alter_column(u'learntogether_collabsession', 'start_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'CollabSession.start_date'
        db.alter_column(u'learntogether_collabsession', 'start_date', self.gf('django.db.models.fields.DateField')())

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
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'course_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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