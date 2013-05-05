# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'learntogether_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('total_points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'learntogether', ['User'])

        # Adding model 'CollabSession'
        db.create_table(u'learntogether_collabsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('course_soure', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('repeats_in_days', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'learntogether', ['CollabSession'])

        # Adding model 'UserGamePoint'
        db.create_table(u'learntogether_usergamepoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.User'])),
            ('point', self.gf('django.db.models.fields.IntegerField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(default='Great Comment', max_length=100)),
            ('collab_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession'], null=True, blank=True)),
        ))
        db.send_create_signal(u'learntogether', ['UserGamePoint'])

        # Adding model 'Achievement'
        db.create_table(u'learntogether_achievement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('badge_icon', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'learntogether', ['Achievement'])

        # Adding model 'UserAchievement'
        db.create_table(u'learntogether_userachievement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.User'])),
            ('achivement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.Achievement'])),
            ('date_achieved', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('collab_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession'], null=True, blank=True)),
        ))
        db.send_create_signal(u'learntogether', ['UserAchievement'])

        # Adding model 'CollabSessionEvent'
        db.create_table(u'learntogether_collabsessionevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collab_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession'])),
            ('session_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('leader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.User'])),
        ))
        db.send_create_signal(u'learntogether', ['CollabSessionEvent'])

        # Adding model 'CollabSessionEventParticipant'
        db.create_table(u'learntogether_collabsessioneventparticipant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collab_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSession'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.User'])),
            ('time_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'learntogether', ['CollabSessionEventParticipant'])

        # Adding model 'GroupMessage'
        db.create_table(u'learntogether_groupmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collab_session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['learntogether.CollabSessionEvent'])),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'learntogether', ['GroupMessage'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'learntogether_user')

        # Deleting model 'CollabSession'
        db.delete_table(u'learntogether_collabsession')

        # Deleting model 'UserGamePoint'
        db.delete_table(u'learntogether_usergamepoint')

        # Deleting model 'Achievement'
        db.delete_table(u'learntogether_achievement')

        # Deleting model 'UserAchievement'
        db.delete_table(u'learntogether_userachievement')

        # Deleting model 'CollabSessionEvent'
        db.delete_table(u'learntogether_collabsessionevent')

        # Deleting model 'CollabSessionEventParticipant'
        db.delete_table(u'learntogether_collabsessioneventparticipant')

        # Deleting model 'GroupMessage'
        db.delete_table(u'learntogether_groupmessage')


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
            'course_soure': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repeats_in_days': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'learntogether.collabsessionevent': {
            'Meta': {'object_name': 'CollabSessionEvent'},
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSession']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']"}),
            'session_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'learntogether.collabsessioneventparticipant': {
            'Meta': {'object_name': 'CollabSessionEventParticipant'},
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSession']"}),
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
            'collab_session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.CollabSession']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'default': "'Great Comment'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['learntogether.User']"})
        }
    }

    complete_apps = ['learntogether']