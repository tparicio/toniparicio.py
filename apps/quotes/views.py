from .models import Author, Book, Quote
from .serializers import AuthorSerializer, BookSerializer, QuoteSerializer
from rest_framework import mixins
from rest_framework import generics


class AuthorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    API endpoints for /authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for authors list
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        API endpoint for author create
        """
        return self.create(request, *args, **kwargs)


class AuthorDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    API endpoints for /authors/{pk}
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for author get
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        API endpoint for author update
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        API endpoint for author delete
        """
        return self.destroy(request, *args, **kwargs)


class BookList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    API endpoints for /books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for list books
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        API endpoint for create book
        """
        return self.create(request, *args, **kwargs)


class BookDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    API endpoints for /books/{pk}
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for get book
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        API endpoint for update book
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        API endpoint for delete book
        """
        return self.destroy(request, *args, **kwargs)


class QuoteList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    API endpoints for /quotes
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for list quotes
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        API endpoint for create quote
        """
        return self.create(request, *args, **kwargs)


class QuoteDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    API endpoints for /quotes/{id}
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        """
        API endpoint for get quote
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        API endpoint for update quote
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        API endpoint for delete quote
        """
        return self.destroy(request, *args, **kwargs)
