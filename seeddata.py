from learntogether.models import *

def initialize():
    user = User(id=1, first_name='Dawa', last_name='Sherpa', nick_name='dminer', total_points=0)
    user.save()
    user = User(id=2, first_name='Micheal', last_name='Kolodny', nick_name='mkolodny', total_points=0)
    user.save()
    user = User(id=3, first_name='Mohit', last_name='Agrawal', nick_name='mohit9', total_points=0)
    user.save()

    collab_session = CollabSession(course_name='Intro to Computer Sciece', course_url='http://khanacademy.org', title='Lets do this')
    collab_session.save()

    collab_event  = CollabSessionEvent(collab_session=collab_session)
    collab_event.save()
