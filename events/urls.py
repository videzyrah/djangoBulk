from django.conf.urls import url
from events import views as event_views

urlpatterns = [
    url(r'^potlucks/$', event_views.potlucks),
    url(r'^(?P<potluck_id>\d+)/$', event_views.potluck),
]
