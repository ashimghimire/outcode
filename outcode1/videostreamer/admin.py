
from django.contrib import admin
from .models import Subscription, Category, Video, WatchHistory, Recommendation

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(WatchHistory)
admin.site.register(Recommendation)
