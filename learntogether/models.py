from django.db import models
from django.db.models import signals
#from south.modelsinspector import add_introspection_rules

# fix South introspection for custom field
#add_introspection_rules([], ["^app\.db\.models.AutoField"])

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField()
    total_points = models.IntegerField(default=0)

class CollabSession(models.Model):
    """
    Template to store session meta info
    """
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=True)
    start_time = models.DateTimeField(auto_now=True)
    repeats_in_days = models.IntegerField(default=7)

class UserGamePoints(models.Model):
    """
    Keep track of a user's points during a given
    game.
    """
    user = models.ForeignKey(User)
    points = models.IntegerField(default=0)
    collab_session_event = models.ForeignKey('CollabSessionEvent', blank=True, null=True) # Point gained in a session

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    badge_icon = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class UserAchievement(models.Model):
    user = models.ForeignKey(User)
    achivement = models.ForeignKey(Achievement)
    date_achieved = models.DateTimeField(auto_now=True)
    reason = models.CharField(max_length=100)
    collab_session = models.ForeignKey('CollabSession', blank=True, null=True) # Point gained in a session

class CollabSessionEvent(models.Model):
    """
    Individiual Session
    """
    collab_session = models.ForeignKey('CollabSession')
    session_date = models.DateField(auto_now=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(null=True)
    leader = models.ForeignKey('User', blank=True, null=True)

class CollabSessionEventParticipant(models.Model):
    collab_session = models.ForeignKey('CollabSessionEvent')
    user = models.ForeignKey(User)
    time_joined = models.DateTimeField(auto_now=True)

def create_usergamepoints(sender, instance, created, raw, update_fields, **kwargs):
    participant = instance
    points = UserGamePoints(user=participant.user,
                            collab_session_event=participant.collab_session)
    points.save()
signals.post_save.connect(create_usergamepoints, sender=CollabSessionEventParticipant, dispatch_uid='create_usergamepoints')

class GroupMessage(models.Model):
    #user = models.ForeignKey(User)
    collab_session = models.ForeignKey('CollabSessionEvent')
    nick = models.CharField(max_length=100)
    message = models.TextField();
    time = models.DateTimeField(auto_now=True) # Date stored in the db

class Course(models.Model):
    category = models.TextField()
    course = models.TextField()
    url = models.TextField()
    course_ext_id = models.TextField(unique=True)
