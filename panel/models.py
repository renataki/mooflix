from django.db import models
import uuid


# Create your models here.
class Status(models.TextChoices):
    Active = "Active"
    Inactive = "Inactive"


class VideoCategory(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sequence = models.DecimalField(max_digits=20, decimal_places=6)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.Inactive)
    url = models.CharField(max_length=255)


    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + self.status


class Video(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=True)
    videoCategory = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=20, decimal_places=6)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.Inactive)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


    def __str__(self):
        return str(self.id) + ", " + self.title + ", " + self.status


class VideoLike(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=True)
    like = models.BooleanField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + ", " + str(self.like) + ", " + str(self.video.id) + ", " + self.video.title + ", " + self.video.status
