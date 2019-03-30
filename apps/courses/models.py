from django.db import models
from apps.timestampable.models import Timestampable


class Platform(Timestampable):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name


class Course(Timestampable):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    finished = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
