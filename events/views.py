from django.shortcuts import render, get_object_or_404
from events.models import Potluck

# Create your views here.
def potlucks(request):
    potlucks = Potluck.objects.all().order_by('-event_date')
    return render(request, 'potlucks.html', { 'potlucks': potlucks })

def potluck(request, potluck_id):
    potluck = get_object_or_404(Potluck, pk=potluck_id)
    return render(request, 'potluck.html', { 'potluck': potluck})
