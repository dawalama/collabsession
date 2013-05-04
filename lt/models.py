from django.db import models

class User(models.Model):
    user_guid = models.CharField(primary_key=True, max_length=32)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    total_points = models.IntegerField()
     
class UserGamePoint(models.Model):
    """
    Store why user was awarded points
    """
    user = models.ForeignKey(User)
    point = models.IntegerField()
    reason = models.CharField(max_length=100)

class Achievement(models.Model):
    achievement_guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=100)
    badge_icon = model.CharField(max_length=100)
    description = model.CharField(max_length=500)

class UserAchievement(models.Model):
    user = models.ForiegnKey(User)
    achivement = models.ForiegnKey(Achievement)
    date_achieved = models.DateTimeField(auto_now=True)

class CollabSession(models.Model):
    """
    Template to store session meta info
    """
    session_guid = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    course_soure = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.DateTimeField()
    repeats_in_days = models.IntegerField()

class CollabSessionEvent(models.Model):
    """
    Individiual Session
    """
    collab_session = models.ForiegnKey(CollabSession)
    session_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    leader = models.ForeignKey(User)
 
class GroupMessage(models.Model):
    message_guid = models.CharField(primary_key=True, max_length=32)
    user = models.ForeignKey(User)
    collab_session = models.ForiegnKey(CollabSession)
    message = models.TextField();
    indicated_time = models.DateTimeField(blank=True) # Date specified in the message
    time = models.DateTimeField(auto_now=True) # Date stored in the db
    
