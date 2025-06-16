from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    debut_year = models.IntegerField()

    def __str__(self):
        return f'{self.name} debut year {self.debut_year}'
