import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'learntogether.settings'

import json
import urllib2
from learntogether.models import *


def init_playlist():
    courses = ['math','science','computer-science','humanities','test-prep']

    data = urllib2.urlopen('http://www.khanacademy.org/api/v1/playlists')
    jdata = json.load(data)

    for data in jdata:
        domain_slug = data['domain_slug']
        if domain_slug is None:
            category = 'general'
        else:
            category = domain_slug

        course = Course(category=category, course=data["title"], url=data["ka_url"], course_ext_id=data["id"], description=data['description'])
        course.save()

def init_course():
    # open the url and the json
    courses = ['math','science','computer-science','humanities','test-prep']

    for course in courses:
        data = urllib2.urlopen('http://www.khanacademy.org/api/v1/topic/'+course)
        j = json.load(data)
        children=j['children']
        for child in children :
            c = Course(category=course, course=child["title"], url=child["url"], course_ext_id=child["id"])
            c.save()



def initialize():
    user = User(id=1, first_name='Dawa', last_name='Sherpa', nick_name='dminer', email='dsherpa@lt.org', password='one', total_points=0)
    user.save()
    user = User(id=2, first_name='Micheal', last_name='Kolodny', nick_name='mkolodny', email='michael@lt.org', password='two', total_points=0)
    user.save()
    user = User(id=3, first_name='Mohit', last_name='Agrawal', nick_name='mohit9', email='mohit@lt.org', password='three', total_points=0)
    user.save()

    course = Course.objects.get(pk=2)
    collab_session = CollabSession(course = course, title='Lets do this')
    collab_session.save()

    collab_event  = CollabSessionEvent(collab_session=collab_session)
    collab_event.save()

    participant = CollabSessionEventParticipant(collab_session=collab_event,
                                                user=user)
    participant.save()

try:
    init_playlist()
except:
    pass
initialize()
