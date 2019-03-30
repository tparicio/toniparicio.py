from django.db import models
from apps.timestampable.models import Timestampable


class SocialNetwork(Timestampable):
    name = models.CharField(max_length=32)
    alias = models.CharField(max_length=64)
    icon = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    position = models.IntegerField()

    def __str__(self):
        return "%s" % self.alias
