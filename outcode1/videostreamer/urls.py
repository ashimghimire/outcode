from django.urls import path
from . import views

urlpatterns = [
    path('<int:video_id>', views.watch_video, name='watch_video'),
]


