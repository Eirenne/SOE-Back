from django.db import models
from django.contrib.auth.models import User
from SOE.users.models import UserProfile


class Emotion(models.Model):
    class Meta:
        verbose_name = "Emotion"
        verbose_name_plural = "Emotions"
        ordering = ('name',)

    name = models.CharField(max_length=32)
    bg_color = models.CharField(max_length=32)
    audio = models.FileField(upload_to='emotions/')

    def __str__(self):
        return self.name


class Record(models.Model):
    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
    date = models.DateField()
    emotions = models.ManyToManyField(Emotion)

    def __str__(self):
        return "{}:{:%Y/%m/%d}".format(self.user.username, self.date)


def song_upload_to(instance, filename):
    return "users/{}/songs/{}".format(instance.user.id, filename)


class Song(models.Model):
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    song = models.FileField(upload_to=song_upload_to)

    def __str__(self):
        return "{}: {:%Y/%m/%d} - {:%Y/%m/%d}".format(self.user.username, self.date_from, self.date_to)
