from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostAPIView


router = DefaultRouter()
router.register('posts', PostAPIView, basename='posts')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:id>', include(router.urls))
]
