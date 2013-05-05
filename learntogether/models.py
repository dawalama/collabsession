from django.db import models

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
    title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    course_soure = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.DateTimeField()
    repeats_in_days = models.IntegerField()
 
class UserGamePoint(models.Model):
    """
    Store why user was awarded points
    """
    user = models.ForeignKey(User)
    point = models.IntegerField()
    reason = models.CharField(max_length=100)
    collab_session = models.ForeignKey(CollabSession, blank=True, null=True) # Point gained in a session

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    badge_icon = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class UserAchievement(models.Model):
    user = models.ForeignKey(User)
    achivement = models.ForeignKey(Achievement)
    date_achieved = models.DateTimeField(auto_now=True)
    reason = models.CharField(max_length=100)
    collab_session = models.ForeignKey(CollabSession, blank=True, null=True) # Point gained in a session

class CollabSessionEvent(models.Model):
    """
    Individiual Session
    """
    collab_session = models.ForeignKey(CollabSession)
    session_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    leader = models.ForeignKey(User)

class CollabSessionEventParticipant(models.Model):
    collab_session = models.ForeignKey(CollabSession)
    user = models.ForeignKey(User)
    time_joined = models.DateTimeField(auto_now=True)

class GroupMessage(models.Model):
    #user = models.ForeignKey(User)
    collab_session = models.ForeignKey(CollabSessionEvent)
    nick = models.CharField(max_length=100)
    message = models.TextField();
    time = models.DateTimeField(auto_now=True) # Date stored in the db
