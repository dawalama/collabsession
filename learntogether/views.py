from __future__ import unicode_literals
import json
import urllib2
import stomp
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.base import View
from django.core import serializers
from django.conf import settings
from dateutil import parser as date_parser
from django.db.models import F
from datetime import datetime
from learntogether.models import CollabSessionEvent, User, Course, UserGamePoints
from learntogether.models import GroupMessage as Message

conn = stomp.Connection()
conn.start()
conn.connect()
conn.subscribe(destination='/messages', ack='auto')

def home(request):
    #current_collab_sessions = CollabSessionEvent.objects.all().filter(session_date=datetime.today()).filter(end_time__gte = datetime.now())
    collab_session_event = CollabSessionEvent.objects.all()
    current_user = User.objects.get(id=request.GET.get('uid'))
    return render_to_response('index.html', {
        'current_sessions': collab_session_event,
        'user': current_user,
        'user_game_points': points,
        })

def index(request):
    """
    handle the index request
    """
    collab_session_id = request.GET.get("cseid")
    user_id = request.GET.get("uid")
    collab_session = CollabSessionEvent.objects.get(id=collab_session_id)
    current_user = User.objects.get(id=user_id)

    messages = Message.objects.all().filter(collab_session=collab_session)
    return render_to_response("collabsession.html", {
        "messages":messages,
        "collab_session_id": collab_session_id,
        "user": current_user,
        "G_APP_ID":settings.GOOGLE_APP_ID,
        "orbited_server":settings.ORBITED_SERVER,
        "orbited_port":settings.ORBITED_PORT,
        "orbited_stomp_port":settings.ORBITED_STOMP_PORT,
    })

def addMessage(request):
    collab_session_id = request.POST.get("cseid")
    nick = request.POST.get("nick", "nobody")
    message = request.POST.get("message", "")
    collab_session = CollabSessionEvent.objects.get(id=collab_session_id)
    msg = Message(collab_session=collab_session, nick=nick, message=message)
    msg.save()
    msg_to_send = json.dumps({"nick":nick, "message":message, "time":msg.time.strftime("%H:%S-%d/%m/%Y")})
    conn.send(msg_to_send, destination='/messages')
    return HttpResponse("ok")

def init_course():
    # open the url and the json
    courses = ['math','science','computer-science','humanities','test-prep']

    for course1 in courses:
        data = urllib2.urlopen('http://www.khanacademy.org/api/v1/topic/'+course1)
        j = json.load(data)
        children=j['children']
        for child in children :
             Course(category=course,course= child["title"],url=child["url"])

class PointsView(View):
    """
    Handle points users give each other during a given
    hangout.
    """
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        """
        Return the points awarded during a given
        collab session.
        """
        collab_session_event = kwargs['collab_session_event']

        # get a json representation of the points users
        # have received in this collab session
        try:
            points = UserGamePoints.objects.get(collab_session_event=collab_session_event)
        except UserGamePoint.DoesNotExist:
            # shouldn't happen
            return HttpResponseBadRequest()
        points = serializers.serialize('json', points)

        return HttpResponse(points, content_type='application/json')

    def post(self, request, *args, **kwargs):
        """
        A user received points during a hangout.
        """
        collab_session_event = kwargs['collab_session_event']
        user_id = kwargs['user_id']

        # give the user 10 points
        num_updated1 = UserGamePoints.objects.filter(collab_session_event=collab_session_event).update(points=F('points')+5)
        num_updated2 = User.objects.filter(id=user_id).update(total_points=F('total_points')+5)

        # make sure only 1 user was updated
        if num_updated != 1 or num_updated2 != 1:
            return HttpResponseBadRequest()

        return HttpResponse()
