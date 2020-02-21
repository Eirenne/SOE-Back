from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.http import Http404
from django.core.files import File
import ffmpeg


class SongViewSet(NestedViewSetMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmotionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.Emotion.objects.all()
    serializer_class = serializers.EmotionSerializer
    permission_classes = ()


class RecordViewSet(NestedViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def get_symphony(self, request, parent_lookup_user=None, pk=None):
        if not request.user:
            raise Http404
        temp_output = "temp_output.mp3"
        date_from = request.data.get("date_from")
        date_to = request.data.get("date_to")
        if not (date_from and date_to):
            # TODO return error
            return Response()
        #
        records = models.Record.objects.filter(user=request.user, date__gte=date_from, date__lte=date_to)\
            .order_by("date")
        emotions = [emotion for record in records for emotion in record.emotions.all()]

        if not emotions:
            return Response()
        #
        try:
            audio_files = []
            for i, emotion in enumerate(emotions):
                ffmpeg.input(emotion.audio.path).output("intermediate{}.mp3".format(i)).overwrite_output().run()
                audio_files.append(ffmpeg.input("intermediate{}.mp3".format(i)))
            # audio_files = [ffmpeg.input(emotion.audio.path) for emotion in emotions]
            ffmpeg.concat(*audio_files, v=0, a=1).output("temp_output.mp3", ).overwrite_output().run()
        except ffmpeg.Error as e:
            # print("ffmpeg error")
            # print(e)
            # TODO return erro
            return Response()
        song = models.Song(user=request.user, date_from=date_from, date_to=date_to)
        song.song.save("{}-{}.mp3".format(date_from, date_to), File(open(temp_output, 'rb')))
        song.save()
        return Response(serializers.SongSerializer(song).data)

