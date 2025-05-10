from django.db import models
from django.contrib.postgres.fields import JSONField


class Movie(models.Model):
    tmbd_id = models.CharField(max_length=50, unique=True)
    imbd_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Timestamps(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='timestamps')
    categories = models.JSONField()
    approved = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

class PendingTimestamps(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='pending_timestamps')
    categories = models.JSONField()
    added_at = models.DateTimeField(auto_now_add=True)
    submitter_ip = models.GenericIPAddressField(null=True, blank=True) 