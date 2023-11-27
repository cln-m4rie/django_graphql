from django.test import TestCase
from api.models import Book
# Create your tests here.

class TestBookRequest(TestCase):
    def test_book(self):
        Book.objects.create(
            title="The Great Gatsby",
            genre="Fiction",
            year=1925,
        )
        response = self.client.get("/api/graphql?query={allBooks{title,genre,year}}")
        self.assertEqual(200, response.status_code,)
        self.assertEqual({
            "data": {
                "allBooks": [
                    {
                        "title": "The Great Gatsby",
                        "genre": "Fiction",
                        "year": 1925
                    }
                ]
            }
        }, response.json())

    def test_create_book(self):
        self.assertEqual(0, Book.objects.count())
        response = self.client.post(
            "/api/graphql",
            data={
                "query": """
                    mutation {
                        createBook(title: "The Great Gatsby", genre: "Fiction", year: 1925) {
                            book {
                                title
                                genre
                                year
                            }
                        }
                    }
                """
            }
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            "data": {
                "createBook": {
                    "book": {
                        "title": "The Great Gatsby",
                        "genre": "Fiction",
                        "year": 1925
                    }
                }
            }
        }, response.json())
        self.assertEqual(1, Book.objects.count())
