from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Author, Book, Quote
from .serializers import QuoteSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_quote(title="", book="", author={"name": "", "last_name": ""}):
        if title != "" and book != "" and author['name'] != "" and author['last_name'] != "":
            author = Author.objects.create(name=author['name'], last_name=author['last_name'])
            book = Book.objects.create(title=title, author=author)
            Quote.objects.create(quote=title, book=book)

    def setUp(self):
        # add test data
        self.create_quote("Veni, vidi, vici", "Julius", {"name": "Julio", "last_name": "Cesar"})
        self.create_quote("En un lugar de la Mancha...", "Don Quijote de la Mancha​", {"name": "Miguel", "last_name": "de Cervantes"})
        self.create_quote("...de cuyo nombre no quiero acordarme", "Don Quijote de la Mancha​", {"name": "Miguel", "last_name": "de Cervantes"})


class GetAllQuotesTest(BaseViewTest):

    def test_get_all_quotes(self):
        """
        This test ensures that all quotes added in the setUp method
        exist when we make a GET request to the quotes/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("quotes-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Quote.objects.all()
        serialized = QuoteSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_quotes_by_book(self):
        """
        This test ensures that all quotes added in the setUp method
        exist when we make a GET request to the quotes/book endpoint
        """
        # hit the API endpoint
        response = self.client.post(
            reverse("quotes-book", kwargs={"version": "v1"}), {"book": "Don Quijote de la Mancha"}
        )
        # fetch the data from db
        book = Book.objects.filter(title="Don Quijote de la Mancha​")[:1].get()
        expected = book.quotes
        serialized = QuoteSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_quote(self):
        """
        This test ensures that one quotes added in the setUp method
        exist when we make a GET request to the quotes/1 endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("quotes-one", kwargs={"version": "v1", "pk": 1})
        )
        # fetch the data from db
        expected = Quote.objects.all()[:1].get()
        serialized = QuoteSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
