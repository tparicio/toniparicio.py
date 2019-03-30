from django.db import models
from apps.timestampable.models import Timestampable


class Enterprise(Timestampable):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
