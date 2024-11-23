
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.utils import timezone

from videostreamer.models import Video, Subscription

def watch_video(request, video_id):
    video = Video.objects.get(id=video_id)
    print(request.user)
    user_subscription = Subscription.objects.filter(user=request.user, end_date__gte=timezone.now()).first()
    if user_subscription is None or not user_subscription.is_active():
        return HttpResponseForbidden("You need an active subscription to watch this video.")
    return render(request, 'watch_video.html', {'video': video})
