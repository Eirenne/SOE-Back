from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Emotion)
class EmotionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    pass
