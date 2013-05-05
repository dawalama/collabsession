import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'learntogether.settings'

from learntogether.models import *

def initialize():
    user = User(id=1, first_name='Dawa', last_name='Sherpa', nick_name='dminer', total_points=0)
    user.save()
    user = User(id=2, first_name='Micheal', last_name='Kolodny', nick_name='mkolodny', total_points=0)
    user.save()
    user = User(id=3, first_name='Mohit', last_name='Agrawal', nick_name='mohit9', total_points=0)
    user.save()

    course = Course(course='Intro to Computer Science', url='http://khanacademy.org', category='computer science')
    course.save()

    collab_session = CollabSession(course = course, title='Lets do this')
    collab_session.save()

    collab_event  = CollabSessionEvent(collab_session=collab_session)
    collab_event.save()

    participant = CollabSessionEventParticipant(collab_session=collab_event,
                                                user=user)
    participant.save()

initialize()
