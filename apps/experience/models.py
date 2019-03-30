from django.db import models
from apps.enterprise.models import Enterprise
from apps.timestampable.models import Timestampable


class Experience(Timestampable):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    job = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    text = models.TextField()
    started_at = models.DateField()
    finished_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.job
