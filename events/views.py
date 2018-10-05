from django.shortcuts import render, get_object_or_404
from events.models import Potluck, Host
import datetime

# Create your views here.
def index(request):
    return render(request, 'events/index.html')


def potlucks(request):
    potlucks = Potluck.objects.all().order_by('-event_date')
    return render(request, 'events/potlucks.html', { 'potlucks': potlucks })

def past(request):
    #Uppercase vs. lowercase screws up alphabetical order_by
    hostQset = Host.objects.all().order_by('-name')
    context = { 'hosts': hostQset }
    return render(request, 'events/pastevents.html', { 'hosts': hostQset })

def upcoming(request):
    now = datetime.datetime.utcnow()
    upcomingevents = Potluck.objects.all().filter(event_date__gte = now.date()).order_by('-event_date')
    context = { 'upcomingevents': upcomingevents }
    return render(request, 'events/upcomingevents.html', context)

def potluck(request, potluck_id):
    potluck = get_object_or_404(Potluck, pk=potluck_id)
    return render(request, 'events/potluck.html', { 'potluck': potluck})
