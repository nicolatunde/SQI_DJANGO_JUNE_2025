from django.shortcuts import render
from .models import Artist

def artistlistening(requests):
    all_artist = Artist.objects.all()
    context = {
        'artists': all_artist,
    }
    return render(requests,'artist/artist.html',context)