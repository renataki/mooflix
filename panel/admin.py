from django.contrib import admin
from .models import Video
from .models import VideoCategory
from .models import VideoLike

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(VideoLike)
