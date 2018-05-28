from django.conf.urls import url
from events import views as event_views

urlpatterns = [
    url(r'^$', event_views.potlucks, name = 'potlucks'),
    url(r'^potlucks/$', event_views.potlucks),
    url(r'^(?P<potluck_id>\d+)/$', event_views.potluck),
    url(r'^upcoming/$', event_views.upcoming, name = 'upcoming'),
    url(r'^pastevents/$', event_views.past, name = 'pastevents'),
]
