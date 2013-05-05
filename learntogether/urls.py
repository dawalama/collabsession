from django.conf.urls import patterns, include, url
from learntogether import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'learntogether.views.home', name='home'),
    url(r'^message/addMessage', 'learntogether.messagebus.addMessage', name='addMessage'),
    url(r'^message/', 'learntogether.messagebus.index', name='messages'),
    (r'^points/(?P<collab_session>[^/]+)(/(?P<user_id>\d+))?$', views.PointsView.as_view()),
)
