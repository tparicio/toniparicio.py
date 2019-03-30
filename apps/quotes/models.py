from django.db import models
from apps.timestampable.models import Timestampable


class Author(Timestampable):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)


class Book(Timestampable):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.title


class Quote(Timestampable):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quote = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.quote
