from __future__ import unicode_literals
import json
import urllib2
import stomp
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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

@login_required
def home(request):
    #current_collab_sessions = CollabSessionEvent.objects.all().filter(session_date=datetime.today()).filter(end_time__gte = datetime.now())
    collab_session_event = CollabSessionEvent.objects.all()
    return render_to_response('index.html', {
        'current_sessions': collab_session_event,
        'user': request.user,
        })

def index(request):
    """
    handle the index request
    """
    collab_session_id = request.GET.get("cseid")
    user_id = request.GET.get("uid")
    collab_session = CollabSessionEvent.objects.get(id=collab_session_id)
    current_user = User.objects.get(id=user_id)
    points = UserGamePoints.objects.filter(collab_session_event=collab_session)
    print points[0].user.total_points

    messages = Message.objects.all().filter(collab_session=collab_session)
    return render_to_response("collabsession.html", {
        "messages":messages,
        "collab_session_id": collab_session_id,
        "user": current_user,
        'user_game_points': points,
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

def browse(request):
    categories = ['math','science','computer-science','humanities','test-prep']
    courses = Course.objects.all()
    courses_in_category = {}
    for c in courses:
        if c.category not in courses_in_category:
            courses_in_category[c.category] = []
        courses_in_category[c.category].append(c)

    return render_to_response('browse.html', {
        'categories': categories,
        'category_courses': courses_in_category})

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
        if num_updated1 != 1 or num_updated2 != 1:
            return HttpResponseBadRequest()

        return HttpResponse()
