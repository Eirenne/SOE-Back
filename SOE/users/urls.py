from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, current_user
from SOE.emotions.views import RecordViewSet, SongViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


api_router = NestedDefaultRouter()

users = api_router.register(r'user', UserViewSet, 'user')
users.register(
   r'records',
   RecordViewSet,
   basename='user-records',
   parents_query_lookups=['user']
)

users.register(
    r'songs',
    SongViewSet,
    basename='user-songs',
    parents_query_lookups=['user']
)

urlpatterns = [
    url(r'^v1/', include(api_router.urls)),
    url(r'^v1/current_user/', current_user),
]
