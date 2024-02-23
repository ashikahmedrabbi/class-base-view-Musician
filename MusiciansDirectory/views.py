from django.shortcuts import render
from Album.models import Album
from musician.models import Musician

def home(request):
    albums = Album.objects.all()
    
    return render(request, 'home.html', {'data': albums })

 