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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    emotions = models.ManyToManyField(Emotion)

    def __str__(self):
        return "{}:{}".format(self.user.first_name, self.date_time)


class Song(models.Model):
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    user = models.ForeignKey(User, on_delete=models.CASCADE)

