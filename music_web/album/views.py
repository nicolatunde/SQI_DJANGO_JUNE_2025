from django.shortcuts import render
from . models import Album
from artist.models import Artist
# Create your views here.






def albumlistening(requests):
    all_artist = Artist.objects.all()
    all_album = Album.objects.all()
    context = {
        'artists': all_artist,
        'albums': all_album,
    }
    return render(requests,'album/album.html',context)




def home(requests):
    return render(requests,'home/home.html')