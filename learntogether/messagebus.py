import json, stomp
from dateutil import parser as date_parser
from datetime import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

from learntogether.models import GroupMessage as Message 
from learntogether.models import CollabSessionEvent, User

conn = stomp.Connection()
conn.start()
conn.connect()
conn.subscribe(destination='/messages', ack='auto')

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
