from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework_extensions.mixins import NestedViewSetMixin
import ffmpeg


class SongViewSet(NestedViewSetMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmotionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = models.Emotion.objects.all()
    serializer_class = serializers.EmotionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RecordViewSet(NestedViewSetMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def get_symphony(self, request, parent_lookup_user=None, pk=None):
        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")
        if not (date_from and date_to):
            print("aralii")

        records = models.Record.objects.filter(user=parent_lookup_user, date_time__gte=date_from, date_time__lte=date_to)\
            .order_by("date_time")
        emotions = [record.emotions for record in records]

        try:
            audio_files = [ffmpeg.input(emotion.audio.path) for emotion in emotions]
            ffmpeg.concat(*audio_files, v=0, a=1).output("alo.mp3").overwrite_output().run()
        except ffmpeg.Error as e:
            print("ffmpeg error")
            print(e)
        return Response()
        # user = self.get_object()
        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
