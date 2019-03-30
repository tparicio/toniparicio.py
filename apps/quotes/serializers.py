from rest_framework import serializers
from .models import Author, Book, Quote


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'link')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'link')
        depth = 1


class QuoteSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Quote
        fields = ('id', 'quote', 'book')
        depth = 2
