from django.db import models
from apps.timestampable.models import Timestampable


class Category(Timestampable):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True)
    position = models.IntegerField()

    def __str__(self):
        return "%s" % self.name


class Skill(Timestampable):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255)
    position = models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return "%s" % self.name
