from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def layout(request):
    return render(request, 'layout.html')

def about(request):
    return render(request, 'about.html')
