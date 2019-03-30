from django.db import models
from apps.timestampable.models import Timestampable


class Project(Timestampable):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name


class Achievement(Timestampable):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    position = models.IntegerField()

    def __str__(self):
        return "%s" % self.description
