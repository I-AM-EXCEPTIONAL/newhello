# myapp/urls.py
from django.urls import path
from .views import IndexView, CameraFeedView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('camera/', CameraFeedView.as_view(), name='camera_feed'),
]
