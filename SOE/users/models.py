from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
