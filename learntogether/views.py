from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.base import View
from django.core import serializers
from django.db.models import F
from datetime import datetime
from learntogether.models import CollabSessionEvent, User

def home(request):
    #current_collab_sessions = CollabSessionEvent.objects.all().filter(session_date=datetime.today()).filter(end_time__gte = datetime.now())
    current_collab_sessions = CollabSessionEvent.objects.all()
    current_user = User.objects.get(id=request.GET.get('uid'))
    return render_to_response('index.html', {
        'current_sessions': current_collab_sessions,
        'user': current_user,
        })

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
            points = UserGamePoint.objects.get(collab_session_event=collab_session_event)
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
        num_updated1 = UserGamePoint.objects.filter(collab_session_event=collab_session_event).update(points=F('points')+10)
        num_updated2 = User.objects.filter(id=user_id).update(total_points=F('total_points')+10)

        # make sure only 1 user was updated
        if num_updated != 1 or num_updated2 != 1:
            return HttpResponseBadRequest()

        return HttpResponse()
