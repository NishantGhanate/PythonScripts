from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=191)
    album_title = models.CharField(max_length=191)
    genre = models.CharField(max_length=85)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10 )
    song_title = models.CharField(max_length = 191 )
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title 
    