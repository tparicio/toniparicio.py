from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Author, Book, Quote
from .serializers import QuoteSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_author(name="", last_name=""):
        if name != "" and last_name != "":
            return Author.objects.create(name=name, last_name=last_name)

    @staticmethod
    def create_book(title="", author=""):
        if title != "" and author != "":
            return Book.objects.create(title=title, author=author)

    @staticmethod
    def create_quote(title="", book=""):
        if title != "" and book != "":
            return Quote.objects.create(quote=title, book=book)

    def setUp(self):
        # add test data
        author = self.create_author('Julio', 'Cesar')
        book = self.create_book('Veni, vidi, vici', author)
        self.create_quote("Veni, vidi, vici", book)
        author = self.create_author('Miguel', 'de Cervantes')
        book = self.create_book('Don Quijote de la Mancha', author)
        self.create_quote("En un lugar de la Mancha...", book)
        self.create_quote("...de cuyo nombre no quiero acordarme", book)


class GetAllQuotesTest(BaseViewTest):

    def test_get_token(self):
        """
        This test ensures that all quotes added in the setUp method
        exist when we make a GET request to the quotes/ endpoint
        """
        token = Token.objects.get(user__username="toni")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token '+token.key)

        # hit the API endpoint
        response = self.client.get(
            reverse("api-quotes-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_quotes(self):
        """
        This test ensures that all quotes added in the setUp method
        exist when we make a GET request to the quotes/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("api-quotes-list", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Quote.objects.all()
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
            reverse("api-quotes-detail", kwargs={"version": "v1", "pk": 1})
        )
        # fetch the data from db
        expected = Quote.objects.all()[:1].get()
        serialized = QuoteSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
