from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import EmotionViewSet, RecordViewSet


api_router = DefaultRouter()
api_router.register(r'emotion', EmotionViewSet, 'emotions')
api_router.register(r'record', RecordViewSet, 'records')

urlpatterns = [
    url(r'^v1/', include(api_router.urls))
]
