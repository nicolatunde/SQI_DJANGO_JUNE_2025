from django.db import models
from artist.models import Artist
# Create your models here.
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="album")
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    
    def __str__(self):
        return f'{self.title} by {self.artist} realease date {self.release_date}'

