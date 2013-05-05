from django.http import HttpResponse
from django.shortcuts import render_to_response
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
