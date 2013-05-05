from django.db import models
from south.modelsinspector import add_introspection_rules

# fix South introspection for custom field
add_introspection_rules([], ["^app\.db\.models.AutoField"])

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    total_points = models.IntegerField()

class CollabSession(models.Model):
    """
    Template to store session meta info
    """
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=True)
    start_time = models.DateTimeField(auto_now=True)
    repeats_in_days = models.IntegerField(default=7)

class UserGamePoint(models.Model):
    """
    Store why user was awarded points
    """
    user = models.ForeignKey(User)
    point = models.IntegerField()
    reason = models.CharField(max_length=100, default='Great Comment')
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
    leader = models.ForeignKey(User, blank=True, null=True)

class CollabSessionEventParticipant(models.Model):
    collab_session = models.ForeignKey('CollabSessionEvent')
    user = models.ForeignKey(User)
    time_joined = models.DateTimeField(auto_now=True)

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
