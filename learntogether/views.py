from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.generic.base import View
from django.core import serializers
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
        hangout.
        """
        collab_session = kwargs['collab_session']
        try:
            points = UserGamePoint.objects.get(collab_session=collab_session)
        except UserGamePoint.DoesNotExist:
            # shouldn't happen
            return HttpResponseBadRequest()
        points = serializers.serialize('json', points)
        return HttpResponse(points, content_type='application/json')

    def post(self, request, *args, **kwargs):
        """
        A user received points during a hangout.
        """
        collab_session = kwargs['collab_session']
        user_id = kwargs['user_id']
