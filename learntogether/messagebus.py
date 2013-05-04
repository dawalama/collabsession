import json, stomp
from dateutil import parser as date_parser
from datetime import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

from learntogether.models import GroupMessage as Message 

conn = stomp.Connection()
conn.start()
conn.connect()
conn.subscribe(destination='/messages', ack='auto')

def index(request):
    """
    handle the index request
    """
    messages = Message.objects.all()
    return render_to_response("index.html", {
        "messages":messages, 
        "orbited_server":settings.ORBITED_SERVER,
        "orbited_port":settings.ORBITED_PORT,
        "orbited_stomp_port":settings.ORBITED_STOMP_PORT,
    })

def addMessage(request):
    user = request.POST.get("user", "nobody")
    message = request.POST.get("message", "")
    post_time = date_parser.parse(request.POST.get("time"))
    msg = Message(user=user, body=message, post_time=post_time)
    msg.save()
    msg_to_send = json.dumps({"user":user,"message":message, "time":date.strftime("%H:%S-%d/%m/%Y")})
    conn.send(msg_to_send, destination='/messages')
    return HttpResponse("ok")
