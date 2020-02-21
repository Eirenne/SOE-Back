from rest_framework import mixins, permissions , status
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from . import models
from . import serializers

from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserViewSet(NestedViewSetMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }

# class UserProfileViewSet(NestedViewSetMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
#     queryset = models.UserProfile.objects.all()
#     serializer_class = serializers.UserProfileSerializer
#     permission_classes = (permissions.IsAuthenticated,)




